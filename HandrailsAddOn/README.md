# **Procedural Tool for Blender**
## **Overview**
The Procedural Tool for Blender is a powerful add-on designed to create customizable structures such as balustrades, stair handrails, glass panels, and railings adaptable to uneven terrains. The tool provides a flexible, user-friendly interface that allows for rapid generation of these elements with just a few inputs, making it ideal for artists and designers looking to speed up their workflow.

### **Features:**
1. Generate balustrades with options for simple or elaborate designs.
2. Create staircase handrails that adapt to different paths, including curves and spirals.
3. Quickly add glass panel railings with realistic glass and metal materials.
4. Adapt railings to uneven terrains, making them follow the landscape seamlessly.

## **Installation**
1. Download the ZIP File:

    Download the ProceduralTool.zip file from the provided link.
2. Install the Add-On in Blender:

    Open Blender.
    Go to Edit > Preferences.
    Click on the Add-ons tab.
    Click Install..., select the ProceduralTool.zip file, and click Install Add-on.
    Once installed, check the box next to the add-on's name to enable it.

## **How to Use the Tool**
After installation, you can find the tool in the 3D View under the Tool Shelf (N key) in the "Handrails" tab. The tool is organized into multiple panels, each with its own function.

### **Panels Overview:**

1. **Balustrade Panel:**

    Create simple or elaborate balustrades.
    Adjust post height, post width, handrail radius, and spacing using the sliders.
    Click "Create Balustrade" to generate the structure.

2. **Staircase Handrail Panel:**

    Set up a staircase by adjusting step count, step dimensions, and handrail height.
    Click "Create Staircase" and then use "Create Stair Posts and Handrail" to generate the posts and handrail.

3. **Glass Panel Railing Panel:**

    Create glass panel railings with adjustable panel length, post height, and handrail size.
    Click "Create Glass Railing".

4. **Uneven Terrain Panel:**

    Create a railing for uneven terrain by selecting a terrain mesh named "UnevenTerrain".
    Click "Create Railing for Uneven Terrain" to automatically adapt the railing to the surface.

## **Technical Details**
### **Modifiers and Nodes Used:**
1. Array Modifier: Used to create repetitive railing sections.
2. Curve Modifier: Used for curved and spiral staircase handrails.
3. Shrinkwrap Modifier: Used to adapt railings to uneven terrain.
4. Geometry Nodes: Considered for procedural adaptation to complex terrains.
### **Material Nodes:**
1. Glass Material: Created with the Glass BSDF Shader for a realistic effect.
2. Metal Material: Created with the Principled BSDF Shader to simulate metal for posts and handrails.

## Contact
For any questions, feel free to reach out to:

Author: Elisa Barba Ortiz
LinkedIn: (https://www.linkedin.com/in/elisa-barba-ortiz)
Email: [elisa.barba@gmail.com]
