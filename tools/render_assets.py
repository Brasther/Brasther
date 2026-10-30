"""Build local profile animations. These are illustrations, not app recordings."""
from __future__ import annotations

import argparse
from html import escape
from io import BytesIO
import math
from pathlib import Path

from PIL import Image, ImageChops
import resvg_py

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
TAU = math.tau
FONT = 'Segoe UI, Arial, sans-serif'


def doc(width, height, title, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><g font-family="{FONT}">{body}</g></svg>'


def hero(t):
    angle = TAU * t
    dots = []
    for i in range(170):
        y = 1 - 2 * (i + .5) / 170
        radius = math.sqrt(1 - y * y)
        theta = i * math.pi * (3 - math.sqrt(5)) + angle
        x, z = radius * math.cos(theta), radius * math.sin(theta)
        rx = x * .94 - y * .34
        ry = x * .34 + y * .94
        depth = (z + 1) / 2
        px, py = 936 + 146 * rx, 188 + 146 * ry
        size = 1 + 1.8 * depth
        color = '#8be4ed' if i % 3 else '#b1a3ff'
        opacity = .17 + .75 * depth
        dots.append((z, f'<circle cx="{px:.2f}" cy="{py:.2f}" r="{size:.2f}" fill="{color}" opacity="{opacity:.3f}"/>'))
    sphere = ''.join(item for _, item in sorted(dots))
    light_x = 930
    light_y = 188
    body = f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#111a2b"/><stop offset="1" stop-color="#0c1220"/></linearGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#c3b4ff"/><stop offset="1" stop-color="#8cd9ed"/></linearGradient>
    <radialGradient id="light"><stop stop-color="#5d56bd" stop-opacity=".24"/><stop offset=".5" stop-color="#385577" stop-opacity=".13"/><stop offset="1" stop-color="#172337" stop-opacity="0"/></radialGradient>
    <clipPath id="frame"><rect width="1200" height="380" rx="22"/></clipPath>
    </defs><g clip-path="url(#frame)">
    <rect width="1200" height="380" fill="url(#bg)"/>
    <ellipse cx="{light_x:.2f}" cy="{light_y:.2f}" rx="400" ry="300" fill="url(#light)"/>
    <text x="60" y="131" fill="#f2f4fb" font-size="70" font-weight="700" letter-spacing="-2">Sebastián</text>
    <text x="58" y="214" fill="url(#name)" font-size="76" font-weight="700" letter-spacing="-2">Salamanca</text>
    <text x="62" y="270" fill="#ccd6e8" font-size="25">Ingeniero en Informática</text>
    <text x="63" y="315" fill="#8e9fbb" font-size="17">Santiago, Chile</text>
    {sphere}</g>'''
    return doc(1200, 380, 'Sebastián Salamanca · Ingeniero en Informática · Santiago, Chile', body)


def flutter_art(t):
    angle = TAU * t
    y = 22 + 3 * math.sin(angle)
    cards = ''
    for i, color in enumerate(('#7cb8f0', '#ba9fea', '#8bd4c9')):
        opacity = .45 + .55 * (.5 + .5 * math.sin(angle + i * TAU / 3))
        cards += f'<rect x="455" y="{y+32+i*32:.2f}" width="24" height="24" rx="5" fill="{color}" opacity="{opacity:.3f}"/><rect x="489" y="{y+37+i*32:.2f}" width="37" height="4" rx="2" fill="#8297b4"/><rect x="489" y="{y+46+i*32:.2f}" width="25" height="3" rx="1.5" fill="#405775"/>'
    return f'<g><rect x="440" y="{y:.2f}" width="105" height="175" rx="20" fill="#101c2e" stroke="#7ebdf0" stroke-width="2"/><rect x="477" y="{y+9:.2f}" width="31" height="4" rx="2" fill="#486682"/>{cards}<rect x="455" y="{y+139:.2f}" width="75" height="20" rx="7" fill="#35698d"/><circle cx="492" cy="{y+149:.2f}" r="3" fill="#a3def7"/></g>'


def sentinel_art(t):
    angle = TAU * t
    bars = ''
    for i in range(11):
        h = 17 + 51 * (.5 + .5 * math.sin(angle * 2 + i * .7))
        bars += f'<rect x="{447+i*8}" y="{110-h/2:.2f}" width="4" height="{h:.2f}" rx="2" fill="#8be1d5" opacity="{.6+.4*math.sin(i*.4)**2:.2f}"/>'
    return f'<path d="M489 25L552 50V102C552 144 526 175 489 194C452 175 426 144 426 102V50Z" fill="#17302f" stroke="#72cfc2" stroke-width="1.6"/>{bars}'


def rocket_art(t):
    p = (1 - math.cos(TAU * t)) / 2
    x = 434*(1-p)**3 + 3*478*(1-p)**2*p + 3*532*(1-p)*p*p + 561*p**3
    y = 170*(1-p)**3 + 3*194*(1-p)**2*p + 3*38*(1-p)*p*p + 51*p**3
    return f'''<path d="M434 170C478 194 532 38 561 51" fill="none" stroke="#625587" stroke-width="2" stroke-dasharray="3 7"/>
    <circle cx="434" cy="170" r="5" fill="#8e7bb8"/><circle cx="561" cy="51" r="5" fill="#b6a1ee"/>
    <g transform="translate({x-15:.2f} {y-17:.2f})"><path d="M0 8L15 0L30 8V27L15 35L0 27Z" fill="#393054" stroke="#c6b4f8" stroke-width="2"/><path d="M0 8L15 16L30 8M15 16V35M7 4L22 12" fill="none" stroke="#c6b4f8" stroke-width="1.5"/></g>'''


def anyshirt_art(t):
    angle = TAU * t
    y = 82 + 16 * math.sin(angle)
    return f'''<defs><clipPath id="print"><rect x="473" y="78" width="47" height="62" rx="4"/></clipPath><linearGradient id="ink"><stop stop-color="#e5b29b"/><stop offset="1" stop-color="#b7a1df"/></linearGradient></defs>
    <path d="M469 35L437 50L424 80L449 95L456 77V185H537V77L544 95L569 80L556 50L524 35C519 55 474 55 469 35Z" fill="#302830" stroke="#d5aa9e" stroke-width="2"/>
    <g clip-path="url(#print)"><rect x="473" y="78" width="47" height="62" fill="#433447"/><circle cx="494" cy="{y:.2f}" r="25" fill="url(#ink)"/><circle cx="514" cy="{y+44:.2f}" r="23" fill="#9992c5" opacity=".8"/></g>'''


PROJECTS = {
    'project-flutter': ('Flutter Shop', 'Tienda multiplataforma', '#172c40', '#79c3f1', flutter_art),
    'project-sentinel': ('Sentinel', 'Audio y moderación para Discord', '#142f2c', '#7bd5c7', sentinel_art),
    'project-rocket': ('Rocket Tracking', 'Seguimiento de envíos', '#25203a', '#b9a0e9', rocket_art),
    'project-anyshirt': ('AnyShirt', 'Poleras personalizadas', '#30252f', '#ddb5a5', anyshirt_art),
}


def project(key, t):
    title, subtitle, color, accent, art = PROJECTS[key]
    body = f'''<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#141d2b"/><stop offset="1" stop-color="{color}"/></linearGradient><clipPath id="frame"><rect width="600" height="220" rx="16"/></clipPath></defs><g clip-path="url(#frame)"><rect width="600" height="220" fill="url(#bg)"/>
    <text x="30" y="88" fill="#f0f3fa" font-size="34" font-weight="600" letter-spacing="-.5">{title}</text>
    <text x="31" y="127" fill="#a6b7cf" font-size="16">{subtitle}</text>
    {art(t)}</g>'''
    return doc(600, 220, f'{title} · Ilustración de {subtitle.lower()}', body)


def render_animation(name, scene, frames, duration, preview):
    images = []
    for i in range(frames):
        svg = scene(i / frames)
        if i == 0:
            (ASSETS / f'{name}.svg').write_text(svg + '\n', encoding='utf-8')
        image = Image.open(BytesIO(resvg_py.svg_to_bytes(svg_string=svg))).convert('RGBA')
        images.append(image)
    rgb = []
    for image in images:
        background = Image.new('RGB', image.size, '#0d1117')
        background.paste(image, mask=image.getchannel('A'))
        rgb.append(background)
    sample = Image.new('RGB', (rgb[0].width, rgb[0].height * 5))
    for row, index in enumerate((0, frames//5, 2*frames//5, 3*frames//5, 4*frames//5)):
        sample.paste(rgb[index], (0, row * rgb[0].height))
    palette = sample.quantize(colors=255, method=Image.Quantize.MEDIANCUT)
    palette_values = palette.getpalette()
    palette_values += [0] * (768 - len(palette_values))
    palette_values[765:768] = [0, 0, 0]
    palette.putpalette(palette_values)
    mask = images[0].getchannel('A').point(lambda alpha: 255 if alpha < 128 else 0)
    # Fixed ordered noise avoids gradient banding without propagating changing
    # diffusion patterns through the otherwise static background.
    bayer = ((0, 8, 2, 10), (12, 4, 14, 6), (3, 11, 1, 9), (15, 7, 13, 5))
    width, height = rgb[0].size
    noise = Image.frombytes('L', (width, height), bytes(
        124 + bayer[y % 4][x % 4] // 2
        for y in range(height) for x in range(width)
    ))
    noise_rgb = Image.merge('RGB', (noise, noise, noise))
    encoded = []
    for image in rgb:
        dithered = ImageChops.add(image, noise_rgb, offset=-128)
        frame = dithered.quantize(palette=palette, dither=Image.Dither.NONE)
        frame.paste(255, mask=mask)
        frame.info['transparency'] = 255
        encoded.append(frame)
    target = ASSETS / f'{name}.gif'
    encoded[0].save(target, save_all=True, append_images=encoded[1:], duration=duration, loop=0,
                    transparency=255, background=255, disposal=1, optimize=False)
    if preview:
        preview.mkdir(parents=True, exist_ok=True)
        for i in (0, frames//4, frames//2):
            images[i].save(preview / f'{name}-{i}.png')
    print(f'{name}: {frames} frames, {target.stat().st_size / 1024:.0f} KB', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frames', type=int, default=80)
    parser.add_argument('--duration', type=int, default=100, help='Milliseconds per frame')
    parser.add_argument('--preview-dir', type=Path)
    args = parser.parse_args()
    if args.frames < 10 or args.duration < 50:
        parser.error('Use at least 10 frames and 50 ms per frame.')
    ASSETS.mkdir(exist_ok=True)
    render_animation('profile-banner', hero, args.frames, args.duration, args.preview_dir)
    for key in PROJECTS:
        render_animation(key, lambda t, key=key: project(key, t), args.frames, args.duration, args.preview_dir)


if __name__ == '__main__':
    main()
