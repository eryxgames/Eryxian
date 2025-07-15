# Sci-Fi Planet Generator for Browser

An interactive, real-time 3D planet visualizer built with **Three.js** and **GLSL**. Create and customize sci-fi planets, from realistic Earth-likes to exotic gas giants with detailed ring systems, all within your browser.


---

## Features

This project leverages simple procedural generation and custom shaders to provide an interactive experience.

#### Planet Generation & Customization
- **Procedural Textures**: Planet surfaces are generated on-the-fly using simplex noise, eliminating the need for static image assets.
- **8 Planet Types**: Instantly switch between presets like Terran, Gas Giant, Volcanic, Ice World, and more.
- **Adjustable Size**: Dynamically scale the planet's radius.
- **Industrial Level**: Control the density and brightness of city lights on the planet's dark side.

#### Atmospherics & Effects
- **Dynamic Atmosphere**: A volumetric-style atmosphere with a realistic glow that reacts to the sun's position.
- **Procedural Clouds**: A moving, distorting cloud layer with simulated weather systems.
- **Concentric Planetary Rings**: A customizable ring system featuring:
    - Realistic concentric stripes and gaps (like the Cassini Division).
    - Adjustable particle density and ring width.
    - Accurate shadows cast by the planet onto the rings.

#### Orbital Systems
- **Moons**: Add up to 8 moons with randomized orbits.
- **Space Traffic**: Simulate orbital traffic with hundreds of small, moving particles.
- **Trajectory Visualization**: Toggleable orbital paths for all moons.

#### Advanced Controls & Visualization
- **Live Shader Editor**: Modify the GLSL vertex and fragment shaders for the planet, rings, or atmosphere in real-time and apply your changes instantly.
- **Multiple Display Modes**: View the planet in various modes for technical analysis:
    - **Shaded**: The full, realistic render.
    - **Minimal**: A simple, lit texture view.
    - **Lat/Long Grid**: Overlays a latitude/longitude grid on the surface.
    - **Heightmap**: Visualizes the underlying noise texture used for terrain.
    - **Point Cloud** & **Wireframe**: Inspect the geometry of the sphere.
- **Scene Import/Export**: Save your entire creation to a JSON file and load it back later to continue your work.

---

## How to Use

#### Mouse Controls
- **Rotate Camera**: Click and drag.
- **Zoom**: Use the mouse scroll wheel.

#### Keyboard Controls
- **`Spacebar`**: Pause / Resume animation.
- **`R`**: Reset camera to the default position.
- **`H`**: Hide / Show the main UI control panel.
- **`S`**: Hide / Show the shader editor panel.

---

## Technical Overview

This application is built with vanilla JavaScript and avoids complex frameworks to keep it lightweight and focused.

- **Core Engine**: **Three.js** is used for the WebGL scene management, camera, lighting, and object rendering.
- **Procedural Generation**: The [Simplex-Noise.js](https://github.com/jwagner/simplex-noise.js) library is used as the basis for all procedural textures, including terrain, clouds, and ring particle distribution. Textures are drawn to a `<canvas>` element in memory and then passed to the shaders.
- **Visuals**: The core visual effects are driven by custom **GLSL (OpenGL Shading Language)** shaders. Key concepts include:
    - **Lambertian and Phong lighting models** for realistic day/night cycles.
    - **Fresnel effects** for the atmospheric glow.
    - **Radial mapping** in the ring shader to create concentric bands from a 1D palette texture.
    - **Uniforms** to pass data (e.g., slider values, time, sun direction) from JavaScript to the GLSL shaders for real-time interactivity.
- **UI**: The user interface is built with **Tailwind CSS** for rapid and clean styling.

---

##  How to Run Locally

This project is a single, self-contained HTML file.

1.  Download the `.html` file.
2.  Open it in a modern web browser (e.g., Chrome, Firefox, Edge).

An internet connection is required on the first run to fetch the Three.js, OrbitControls, Simplex-Noise, and Tailwind CSS libraries from their respective CDNs.