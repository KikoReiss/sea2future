# sea2future

[![Generic badge](https://img.shields.io/badge/version-0.2.2-green.svg)](https://shields.io/)

This addon was developed with the purpose of giving Blender the capacity of a visualisation of the attitude of a USV (Unmanned Surface Vehicle). Being able to do it in real time, or by reading a file that would contain information about it.

![](./doc/example.gif)

## Installation

1. Download the zip file, do not unzip it.
2. Go to Blender's <b>user preferences</b>.
3. Open the <b>Addons</b> tab, click <b>install</b> and select the zip file.
4. Check if the box next to it's name is enabled.

The addon will be visible in the <b>Collection Properties</b>.

## Usage

Currently the addon has 2 different features.

- <b>Live View</b>

  Allows a real time visualization of a body attitude by changing the rotation of an object.

  To use this feature the user just needs to choose the <b>connection type</b> from the dropdown menu and then fill the form that appears. Then press the button and the object that is currently selected will begin to rotate accordingly to the values that it receives.

- <b>Load File</b>

  Allows the import of a file that contains information about the attitude of a body.

  To use this feature the user just needs to choose the <b>attitude type</b> from the dropdown menu and then load the file that contains the attitude information. Then press the button and a group of keyframes where the objet rotation change will be added to the selected objet.
