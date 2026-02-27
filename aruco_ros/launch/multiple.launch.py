from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    single_launch = PathJoinSubstitution([
        FindPackageShare('aruco_ros'),
        'launch',
        'single.launch.py'
    ])

    drone = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(single_launch),
        launch_arguments={
            # core params
            'node_name': 'aruco_drone',
            'camera_frame': 'mavic_1/camera_link',
            'marker_id': '3',
            'marker_size': '0.1651',  # To check
            'eye': 'left',
            'marker_frame': 'aruco_marker_frame_left_drone',
            'reference_frame': 'mavic_1/camera_link',
            'corner_refinement': 'LINES',

            # remaps
            'remap_camera_info_to': '/mavic_1/image/camera_info',
            'remap_image_to': '/mavic_1/camera/current_image',
        }.items(),
    )

    gs = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(single_launch),
        launch_arguments={
            # core params
            'node_name': 'aruco_gs',
            'camera_frame': 'gs/camera_link',
            'marker_id': '3',
            'marker_size': '0.1651', # To check
            'eye': 'left',
            'marker_frame': 'aruco_marker_frame_left_gs',
            'reference_frame': 'gs/camera_link',
            'corner_refinement': 'LINES',

            # remaps
            'remap_camera_info_to': '/visual_servo/goal_camera_info',
            'remap_image_to': '/visual_servo/goal_image',
        }.items(),
    )

    return LaunchDescription([drone, gs])