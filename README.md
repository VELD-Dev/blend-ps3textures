# The Blend-PS3Textures have been discontinued !
[**Click here to go to the new equivalent !**](https://github.com/VELD-Dev/raclette-and-tank "Raclette & Tank Importer")  
**Raclette & Tank Importer** is a Blender plugin made to extract maps/levels from **Ratchet & Clank games (and optional Resistance 2 and 3)**, direclty from the source files.  
The main point of it is to do what [**Lunacy Level Editor**](https://github.com/NefariousTechSupport/Lunacy "Nefarious Tech Support's Lunacy Level Editor") doesn't do, so entire level exporting, etc.  
Yes, because **Lunacy** is a **Level-Editor**, not a **Level-Exporter**, so here's **Raclette & Tank Importer**, made to extract maps from R&C Future series games, and put it right into you Blender Project.  
This plugin is especially made for fans who want to make animations, "SFM" music clips, and even fangames.  
Of course, you're pleased to respect all the copy rights of Insomniac Games and SCIE.

# Blend-PS3Textures
Blend-PS3Textures (but I call it PS3T `/pset/`) is a plugin for Blender that allow people to "re-materialize" exported maps or models from the [LombaxToes Level Editor](https://github.com/NefariousTechSupport/LombaxToes) *(or any other way to extract mesh & textures from a PS3 game, that the plugin is compatible with)* to generate every materials using their respective textures. Example:
- Ratchet & Clank: Tools of Destruction has these textures: 
  - `1654_C.bmp` (Base Colour)
  - `1654_N.bmp` (Normals)
  - `1654_E.bmp` (Specular/Rougness/Metalness/Emissive) \[**INSOMNIAC ENGINE 2.0** and **3.0**]

This will make a material file `map.mtl` that link all the textures of the map `map.obj`, and show the right materials into the engine (blender, etc...)  

⚠ The loading may take a while, or can crash on some low configs. Be careful before using it, make a backup of the map files.

# Software info
**Python version**: `v3.10.5^`  
**Blender version**: `v3.2.0^`  

## Important stuff
U have to know that this is open-source and that the plugin is kinda linked to the **[NefariousTechSupport/LombaxToes](https://github.com/NefariousTechSupport/LombaxToes)** software, I'm making this to EASILY glue EVERY textures to their specular, their normals, etc... and make the whole map exportable with the material - `.mtl` file - ready for *Unreal Engine* or any other 3D engine.

## Starting working on the plugin

* [Starting with Python](https://www.python.org/about/gettingstarted/)
* [Quickstart with Blender API](https://docs.blender.org/api/current/info_quickstart.html)
* [Full Blender API Doc.](https://docs.blender.org/api/current/)

## Some explanation about the material file
This is the hierarchy of a material file:
- `map.obj`
- `map.mtl`
  - `material_256` (viewable into Blender)
    - link to `tex_256_C` as `base_colour`
    - link to `tex_256_E` as `roughness+specular`
  - `material_257` (viewable into Blender)
    - link to `tex_257_C` as `base_coulour`
    - link to `tex_257_E` as `specular_(only)`
    - link to `tex_257_N` as `normals`
  - etc...
- `tex_256_C.png`
- `tex_256_E.png`
- `tex_257_C.png`
- `tex_257_E.png`
- `tex_257_N.png`
- etc...  

That's all you need to know, the mtl file contains the material data for every mesh and submeshes of a model
