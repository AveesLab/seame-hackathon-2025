from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='piracer_demo',
            executable='control_node',
            name='control_node',
            output='screen'
        ),
        Node(
            package='piracer_demo',
            executable='todo_node',
            name='todo_node',
            output='screen'
        ),
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen'
        ),
    ])
