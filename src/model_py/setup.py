from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'model_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        (os.path.join('share', package_name,'world'), glob('world/*')),
        (os.path.join('share', package_name,'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name,'config'), glob('config/*')),


    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nikhil',
    maintainer_email='nikhileshkumar713@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'laser_frame_publisher=model_py.frame:main',
            'test_joy=model_py.joytest:main',
            'keyboard_listener=keyboard_node:main',
            'intel_publisher = model_py.real_pub:main '
        ],
    },
)
