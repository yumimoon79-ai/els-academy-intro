"""실제 학원 사진을 슬롯 파일명으로 변환/최적화하여 배치."""
from pathlib import Path
from PIL import Image, ImageOps

assets = Path(__file__).resolve().parent / "assets"

# 원본 파일명 -> 목표 슬롯 파일명
mapping = {
    "KakaoTalk_20241202_144054904.jpg": "hero.jpg",
    "ChatGPT Image 2026년 7월 18일 오전 10_44_19.png": "director.jpg",
    "KakaoTalk_20250407_173904915_02.jpg": "english-class.jpg",
    "KakaoTalk_20241202_144105753.jpg": "math-class.jpg",
    "스크린샷 2026-07-23 010715.png": "learning-system.jpg",
    "KakaoTalk_20241203_214626284.jpg": "academy-space.jpg",
}

MAX = 1600

for src_name, dst_name in mapping.items():
    src = assets / src_name
    if not src.exists():
        print("MISSING:", src_name)
        continue
    img = Image.open(src)
    img = ImageOps.exif_transpose(img)  # 휴대폰 회전 정보 반영
    if img.mode in ("RGBA", "P", "LA"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[-1])
        img = bg
    else:
        img = img.convert("RGB")
    img.thumbnail((MAX, MAX), Image.LANCZOS)
    dst = assets / dst_name
    img.save(dst, "JPEG", quality=85, optimize=True)
    print(f"{dst_name:22s} <- {src_name[:30]:30s} {img.size}")

print("done")
