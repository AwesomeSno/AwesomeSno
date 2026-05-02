```bash
$ cat harinandan.profile
# -----------------------------------------------
# Name    : Harinandan J V
# Alias   : awesomesno
# Age     : 18
# Loc     : Kerala, India
# Orgs    : AxeomLabs  |  The Shadow Company
# URL     : harinandan.in
# Status  : Debugging 6 impossible projects at 2am
# -----------------------------------------------
# Recent activity:
#   Wrote a bootloader         [done]
#   Built an x64 CPU emulator  [done]
#   Started a game engine      [in progress, send help]
#   Automated my house         [done, it works, mostly]
#   Built a physics simulator  [objects make sounds now. yes on purpose]
#   Writing an OS from scratch [you read that right]
# -----------------------------------------------
$
```

<br>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=32&duration=3500&pause=99999&color=39FF14&center=true&vCenter=true&repeat=false&width=500&lines=hi.+i'm+harinandan." />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=3500&pause=99999&color=39FF14&center=true&vCenter=true&repeat=false&width=828&lines=I%27m+18+year+old+from+Kerala+who+thought+%22building+an+OS+from+scratch%22+was+a+reasonable+thing+to+do" />
</p>

<br>

<p align="center">
  <img src="https://img.shields.io/badge/age-18-39FF14?style=flat-square&labelColor=0d0d0d" />
  <img src="https://img.shields.io/badge/location-Kerala%2C_India-39FF14?style=flat-square&labelColor=0d0d0d" />
  <img src="https://img.shields.io/badge/sleep_schedule-what's_that%3F-ff4444?style=flat-square&labelColor=0d0d0d" />
  <img src="https://img.shields.io/badge/status-building_too_many_things-39FF14?style=flat-square&labelColor=0d0d0d" />
  <img src="https://komarev.com/ghpvc/?username=AwesomeSno&label=people+who+ended+up+here&color=39FF14&style=flat-square&labelColor=0d0d0d" />
</p>

---

## ok so here's the deal

i'm self-taught. no cs degree, no bootcamp, no roadmap. i just started building things that seemed too hard and kept going until they weren't.

i write operating systems from bare metal, binary translators for x64 executables, game engines from scratch, physics simulators, smart home automation systems, and apparently also robotic arms that respond to hand gestures. not for work. just because i want to understand how everything works at the lowest possible level. if i can't build it from scratch, i don't feel like i really understand it.

i run **AxeomLabs** (proprietary systems, research-grade software) and **The Shadow Company** (a tech collective for people who actually build things). both are real. both are active. both have more going on than is public right now.

---

## what i'm actually building rn

> not "what i'm interested in." what i am literally working on right now.

<table>
<tr>
<td width="50%" valign="top">

### 🖥️ Untitled OS
`C` `Assembly` `bare metal` `in dev`

an operating system built from bare metal. no Linux base, no borrowed kernel, no shortcuts. custom bootloader, memory manager, scheduler, the whole thing. the goal is an OS where privacy isn't a setting you toggle, it's just how the system works by design.

yes i know how that sounds. yes i'm still doing it. (no name yet. it'll get one when it deserves one.)

</td>
<td width="50%" valign="top">

### 🎮 Project Engine
`C++20/23` `AxeomLabs` `proprietary`

a unified game engine AND scientific simulation platform in one codebase. seven major subsystems. targets nine platforms including consoles. one of those subsystems is a biomechanics engine with actual Hill-type muscle models and injury simulation. yeah. i'm also pulling in parts of Godot for faster development on certain areas so i don't burn time reinventing things that are already solid. the core architecture is still mine.

this one's going to take a while but i'm not cutting corners on any of it.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🪟 ProWin
`C++` `Swift` `open source` `v0.15.0`

loads and runs Windows x64 PE32+ binaries directly on macOS. no VM. i wrote the dynamic binary translator myself. translates DirectX to Metal, XAudio2 to AVFoundation, XInput to GameController in real time.

currently handles simple binaries correctly. DirectX pipeline is next. i'm also thinking about pulling in parts of Wine for some of the compatibility layer work, though that's not a final decision yet. long road but it works.

</td>
<td width="50%" valign="top">

### ⚡ Zero Invasion
`C++20` `pre-alpha`

real-time 2D/3D physics simulation platform. rigid bodies, soft bodies, joints, materials, wind, gravity. the part nobody else does: every object emits sound based on its material, velocity, and collision force. physics-driven audio synthesis. in real time.

runs natively on Metal, Vulkan, and OpenGL. there's a chance this gets absorbed into Project Engine as a subsystem down the line. nothing decided yet.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔐 ZeroVault
`privacy app` `in dev`

encrypted notes app. no cloud, no sync, no accounts, no telemetry, nothing leaves your device. ever. made it because i wanted a notes app that actually means it when it says local-only and not "local unless we decide otherwise."

</td>
<td width="50%" valign="top">

### 🏠 Home Automation System
`ESP32` `prototyped`

whole-house automation with lighting, security, environmental monitoring, and access control. no SmartThings, no Alexa, no subscription, no cloud. just hardware i wired and code i wrote.

</td>
</tr>
</table>

<details>
<summary><b>there's one more (click if you're curious)</b></summary>

<br>

### 🤖 Robotic Arm
`Arduino` `OpenCV` `prototyped`

3D-printed robotic arm that mirrors my hand in real time using OpenCV-based hand gesture recognition. working on a custom controller UI separately but that's on hold for now, got bigger things going on.

the gesture control is the cool part anyway.

<br>
</details>

---

## the honest checklist

```
DONE:
[x]  written a bootloader in assembly
[x]  built a working x64 CPU emulator from scratch
[x]  designed a 7-module cross-platform game engine architecture
[x]  automated an entire house with custom ESP32 code
[x]  made a robotic arm respond to hand gestures via computer vision
[x]  built a physics sim where objects generate sound from their material
[x]  shipped an encrypted notes app with zero external dependencies
[x]  started a proprietary software lab  (AxeomLabs)
[x]  started a tech collective           (The Shadow Company)

STILL COOKING:
[ ]  Untitled OS first boot                   // getting there
[ ]  Project Engine running a game            // it's a marathon
[ ]  ProWin running a full DirectX title      // making real progress
[ ]  Zero Invasion v1.0 public release        // steady
[ ]  sleep a normal amount                    // not looking good honestly
```

---

## stuff i know

```
languages    C  |  C++  |  C#  |  Assembly  |  Python  |  Swift  |  Bash  |  HTML/CSS

gpu apis     Metal  |  Vulkan  |  OpenGL  |  DirectX 12

tools        CMake  |  Ninja  |  Xcode  |  Make  |  Git

frameworks   OpenCV  |  Unreal Engine  |  Unity  |  SwiftUI  |  Dear ImGui  |  JoltPhysics

hardware     Arduino  |  ESP32  |  3D printing

domains      OS development       |  binary emulation       |  systems programming
             computer vision      |  embedded systems       |  game engine architecture
             cybersecurity        |  robotics               |  physics simulation
             AI + ML              |  real-time audio        |  networking
```

---

## proof i exist and actually commit

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=AwesomeSno&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&bg_color=0d0d0d&title_color=39FF14&icon_color=39FF14&text_color=777777" width="49%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=AwesomeSno&layout=compact&hide_border=true&bg_color=0d0d0d&title_color=39FF14&text_color=777777" width="49%" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=AwesomeSno&hide_border=true&ring=39FF14&fire=39FF14&currStreakLabel=39FF14&background=0d0d0d&sideLabels=ffffff&dates=dddddd&currStreakNum=ffffff&sideNums=ffffff" width="65%" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=AwesomeSno&bg_color=0d0d0d&color=39FF14&line=39FF14&point=ffffff&area=true&area_color=0d0d0d&hide_border=true" width="95%" />
</p>

---

## one thing i actually believe

> *"if you don't understand how it works at the lowest level, you don't really understand it."*

most people wait until they're "ready" to start something hard. i don't think that ever comes. so i just start, go learn what i'm missing, and come back. that's how you end up writing bootloaders at 17 and not thinking it's weird.

---

## find me

<p align="center">
  <a href="https://harinandan.in">
    <img src="https://img.shields.io/badge/harinandan.in-website-39FF14?style=for-the-badge&logo=googlechrome&logoColor=black&labelColor=0d0d0d" />
  </a>
  <a href="https://in.linkedin.com/in/snox">
    <img src="https://img.shields.io/badge/snox-linkedin-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d0d0d" />
  </a>
  <a href="https://instagram.com/snozuuz">
    <img src="https://img.shields.io/badge/snozuuz-instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white&labelColor=0d0d0d" />
  </a>
  <a href="mailto:harinandanjv@gmail.com">
    <img src="https://img.shields.io/badge/harinandanjv@gmail.com-email-ff4444?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d0d0d" />
  </a>
</p>

---

<br>

<p align="center">
  <sub>if you want to build something genuinely ambitious, you know where to find me.</sub><br><br>
  <sub>if something here seems impossible for a 18 year old -- that's exactly why i'm doing it.</sub>
</p>
