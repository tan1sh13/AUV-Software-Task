from setuptools import find_packages, setup
from setuptools import setup
import os
from glob import glob
package_name = 'chat_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/chat_pkg']),
    ('share/chat_pkg', ['package.xml']),
    (os.path.join('share', 'chat_pkg', 'msg'),
        glob('msg/*.msg')),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tanish',
    maintainer_email='tanish70007@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
   entry_points={
    'console_scripts': [
        'chat_node = chat_pkg.chat_node:main',
        'publisher_node = chat_pkg.publisher_node:main',
        'processor_node = chat_pkg.processor_node:main',
        'output_node = chat_pkg.output_node:main',
	'commander_node = chat_pkg.commander_node:main',
	'navigator_node = chat_pkg.navigator_node:main',
	'vision_node = chat_pkg.vision_node:main',
    ],
},
)
