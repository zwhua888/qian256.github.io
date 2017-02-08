---
layout: post
title: ARToolKit on HoloLens
---

[HoloLens](https://www.microsoft.com/microsoft-hololens/en-us) is fascinating in terms of holographic display and in-room localization, but the capability of the front-facing camera ([locatable camera](https://developer.microsoft.com/en-us/windows/holographic/locatable_camera)) is not fully utilized for potential augmented reality applications.

### Why not Vuforia?

[Vuforia]() released it support for HoloLens several month ago with Vuforia 6. Vuforia has its feature-based tracking, extended tracking mode, simple 3D model tracking, etc. However, there is several potential problems with Vuforia, from a developer point of view.

* Limited update rate, not intended for fast moving object.
* Lack of accuracy.
* Closed-source software, you have to get your finger-crossed for everything.
* Is charged.

### ARToolKit

Since [ARToolKit]() has served AR/VR for more than 10 years, and it is open-source, it would be nice to have it running on HoloLens. The obstacles towards this goal are quite clear as well:

* Universal Windows has a whole different set of tools and run-time libraries. The dependencies of existing ARToolKit does not exist on UWP, such as pthreads, video libraries, opencv.
* ARToolKit is written in native C/C++ code, and an additional wrapper is needed for development on Unity, which is recommended for HoloLens. (If you are not good at Direct3D, and Windows App)

**Luckily, after spending about a week on this, I successfully get some pieces of code written, and actually make ARToolKit runs on HoloLens, at about 40 fps.**

The repository is called [HoloLensARToolKit]() on Github.

### Demo

#### Hiro and Kanji

<p class="full-width">
	<img src="https://cloud.githubusercontent.com/assets/8185982/22130806/ade7e8ac-de7c-11e6-82ff-d1b31caef17f.jpg" alt="Hiro and Kanji" style="width:35.3%;padding:0.5rem" align="right"/>
	<img src="https://cloud.githubusercontent.com/assets/8185982/22130805/ade4ac96-de7c-11e6-91fb-a3be5ad5d559.jpg" alt="Hiro and Kanji" style="width:35%;padding:0.5rem" align="right"/>
</p>

The above shows the screenshot of HoloLens taken via HoloLens Device Portal.
There are several things here to pay attention to:

* The image plane visualizes the current camera feed.
* Two markers are used: the traditional ARToolKit Hiro and Kanji marker.
* The cubes on top represents the rotation of the tracked markers.
* Frame rate of tracking and rendering are both about 40 fps.
* Confidence values of tracking are shown in the top right corner.

#### Multi Marker

<p class="full-width"><img src="https://cloud.githubusercontent.com/assets/8185982/22189679/0a6f8a6e-e0ec-11e6-8563-ecae01e7d294.jpg" alt="Multi Marker" style="width:60%;" align="right"/></p>

ARToolKit-style multi marker pattern is supported. Individual cubes represent the tracking result of each barcode marker, and the while plane represents the tracking result of the multi marker as whole.


#### Cube Marker


<p class="full-width"><img src="https://cloud.githubusercontent.com/assets/8185982/22190907/907d311c-e0f4-11e6-84b4-91b47586b008.jpg" alt="Cube Marker" style="width:60%;" align="right"/></p>

As a special case of multi marker pattern, the cube marker is supported on HoloLensARToolKit as well.


### Finally
With ARToolKit integrated with HoloLens, many more augmented reality applications are possible. If you are AR/VR developer, you must see what I mean here.

Thanks for reading. <img class="inline" src="/public/LQ144x144.png" alt="LQ" style="width:1.5rem;height:1.5rem;" />
