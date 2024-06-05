# Import necessary modules from the launch package
import os
from launch import LaunchDescription
from launch_ros.actions import Node, SetParameter
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration

# Define the main function that generates the launch description
def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf_file_name = 'robot_arm_urdf.urdf'
    rviz_file_name = 'config.rviz'

    urdf_path = os.path.join(
        get_package_share_directory('solid2ROS'),
        'urdf',
        urdf_file_name)
    
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    rviz = LaunchConfiguration('rviz_config',
                               default=str(os.path.join(
                                   get_package_share_directory('solid2ROS'), 'config', rviz_file_name)))

    return LaunchDescription([
        DeclareLaunchArgument(
            'urdf',
            default_value=urdf_path,
            description='path to urdf file'
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen',
            parameters=[{'robot_description': robot_desc}]),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]),
        # Launch the joint_state_publisher node
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=['-d', rviz]),
    ])