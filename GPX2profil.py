import os
import gpxpy
import matplotlib.pyplot as plt
from geopy.distance import geodesic
import numpy as np
from scipy.signal import savgol_filter

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def get_output_png_path(gpx_file_path):
    gpx_folder, gpx_filename = os.path.split(gpx_file_path)
    gpx_filename_without_extension = os.path.splitext(gpx_filename)[0]
    return os.path.join(gpx_folder, f"{gpx_filename_without_extension}_profil_altitude.png")

def find_start_point(gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            found_start_point = False
            for point in segment.points:
                if point.comment and "départ" in point.comment.lower() and "réel" in point.comment.lower():
                    found_start_point = True
                if found_start_point:
                    return point
    return None

def plot_altitude_profile(gpx_file_path, image_width=1100, image_height=150,
                          dpi=72, background_color='#FFFFFF', fill_color='#FFFFFF',
                          line_color='black', smooth_factor=3, top_margin=10, flatten_factor=0.7):
    # Charger le fichier GPX
    with open(gpx_file_path, 'r', encoding='utf-8') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    # Trouver le point de départ réel
    start_point = find_start_point(gpx)

    if not start_point:
        raise ValueError("Le point de départ réel n'a pas été trouvé dans le fichier GPX.")
    
    # Initialiser la variable found_start_point
    found_start_point = False

    # Extraire les points d'altitude et de longitude du parcours à partir du point de départ réel
    altitude_data = []
    distance_data = []
    prev_point = None
    total_distance = 0.0

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if point == start_point:
                    found_start_point = True
                elif found_start_point:
                    altitude_data.append(point.elevation)
                    if prev_point is not None:
                        total_distance += calculate_distance((prev_point.latitude, prev_point.longitude),
                                                             (point.latitude, point.longitude))
                    distance_data.append(total_distance)

                prev_point = point

    # Interpolation pour lisser les données d'altitude
    distance_smooth = np.linspace(min(distance_data), max(distance_data), len(altitude_data))
    altitude_smooth = savgol_filter(altitude_data, window_length=smooth_factor*2+1, polyorder=2)

    # Appliquer l'effet d'aplatissement de haut en bas
    max_altitude = max(altitude_smooth)
    altitude_smooth = (altitude_smooth / max_altitude) ** flatten_factor * max_altitude

    # Créer une figure sans axes avec la taille de l'image
    fig, ax = plt.subplots(figsize=(image_width/dpi, image_height/dpi), dpi=dpi)
    ax.axis('off')
    ax.set_facecolor(background_color)
    
    # Tracer le profil d'altitude sous forme de polygone rempli
    points = np.column_stack((distance_smooth, altitude_smooth))
    points = np.vstack([[points[0, 0], 0], points, [points[-1, 0], 0]])
    ax.fill(points[:, 0], points[:, 1], fill_color, edgecolor='none')

    # Supprimer les marges latérales
    ax.set_xlim(min(distance_smooth), max(distance_smooth))
    ax.set_ylim(0, max(altitude_smooth) + top_margin)

    # Obtenir le chemin de sortie PNG
    output_png_path = get_output_png_path(gpx_file_path)

    # Sauvegarder l'image avec fond transparent
    plt.savefig(output_png_path, transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()

    return output_png_path

if __name__ == "__main__":
    gpx_file_path = "c:/Users/dorian blacks/Desktop/GPX2Profil/Etape4.gpx"
    output_png_path = plot_altitude_profile(gpx_file_path, fill_color='#FFFFFF', smooth_factor=90, flatten_factor=0.5, top_margin=600)
    print(f"L'image du profil d'altitude a été générée et enregistrée sous {output_png_path}.")
