# Blend-PS3Textures
Blend-PS3Textures is a plugin for Blender that allow people to use exported maps from the [LombaxToes Level Editor](https://github.com/NefariousTechSupport/LombaxToes) to generate every materials using their respective textures. Example:
- Ratchet & Clank: Tools of Destruction has these textures: 
  - `1654_C.bmp` (Base Colour)
  - `1654_N.bmp` (Normals)
  - `1654_S.bmp` (Specular)
  - `1654_R.bmp` (Rougness)
  - (In reality I don't know yet how the textures are)
This will make a material file `map.mtl` that link all the textures of the map `map.obj`, and show the right materials into the engine (blender, etc...)
⚠ The loading may take a while, or can crash on some low configs. Be careful before using it, make a backup of the map files.

## Important stuff
U have to know that this is open-source and that the plugin is kinda linked to the **[NefariousTechSupport/LombaxToes](https://github.com/NefariousTechSupport/LombaxToes)** software, I'm making this to EASILY glue EVERY textures to their specular, their normals, etc... and make the whole map exportable with the materials ready for *Unreal Engine* or any other 3D engine.
This is of course Python, because Blender is Python.

## Starting working on the plugin

* [Starting with Python](https://www.python.org/about/gettingstarted/)
* [Quickstart with Blender API](https://docs.blender.org/api/current/info_quickstart.html)
* [Full Blender API Doc.](https://docs.blender.org/api/current/)
