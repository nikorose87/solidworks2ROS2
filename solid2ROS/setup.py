from setuptools import find_packages, setup
from glob import glob

package_name = 'solid2ROS'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all files in the launch directory
        ('share/' + package_name + '/launch', glob('launch/*')),
        # Include all files in the meshes directory
        ('share/' + package_name + '/meshes', glob('meshes/*')),
        # Include all files in the urdf directory
        ('share/' + package_name + '/urdf', glob('urdf/*')),
        # Include all files in the config directory
        ('share/' + package_name + '/config', glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nikorose',
    maintainer_email='nikolay@mvnifest.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
