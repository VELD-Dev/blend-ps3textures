# Blend-PS3Textures
Blend-PS3Textures (but I call it PS3T `/pset/`) is a plugin for Blender that allow people to "re-materialize" exported maps or models from the [LombaxToes Level Editor](https://github.com/NefariousTechSupport/LombaxToes) *(or any other way to extract mesh & textures from a PS3 game, that the plugin is compatible with)* to generate every materials using their respective textures. Example:
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

## Some explanation about the material file
This is the hierarchy of a material file:
- `map.obj`
- `map.mtl`
  - `material_1` (viewable into Blender)
    - link to `tex_256_C` as `base_colour`
    - link to `tex_256_R` as `roughness`
  - `material_2` (viewable into Blender)
    - link to `tex_257_C` as `base_coulour`
    - link to `tex_257_S` as `specular`
  - etc...
- `tex_256_C.png`
- `tex_256_R.png`
- `tex_257_C.png`
- `tex_257_S.png`
- etc...  

That's all you need to know, the mtl file contains the material data for every mesh and submeshes of a model
