"""ELS 학원소개 placeholder 이미지 생성 (Windows / 맑은 고딕).
실행: python _make_placeholders.py
실제 사진으로 교체하기 전까지 사용할 임시 이미지를 assets/ 에 만든다.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

base = Path(__file__).resolve().parent
assets = base / "assets"
assets.mkdir(parents=True, exist_ok=True)

REG = r"C:\Windows\Fonts\malgun.ttf"
BOLD = r"C:\Windows\Fonts\malgunbd.ttf"


def get_font(size, bold=False):
    path = BOLD if (bold and Path(BOLD).exists()) else REG
    return ImageFont.truetype(path, size)


def make_placeholder(filename, title, subtitle, size=(1600, 1000), accent=(37, 99, 235)):
    img = Image.new("RGB", size, (246, 249, 252))
    d = ImageDraw.Draw(img)
    w, h = size

    d.ellipse((-180, -160, 650, 640), fill=(224, 238, 255))
    d.ellipse((1040, 480, 1770, 1200), fill=(224, 247, 239))
    d.rounded_rectangle((140, 135, w - 140, h - 135), radius=50,
                        fill=(255, 255, 255), outline=(218, 226, 236), width=4)
    d.rounded_rectangle((205, 210, 335, 340), radius=28, fill=accent)

    title_font = get_font(78, bold=True)
    sub_font = get_font(35)
    hint_font = get_font(28)

    d.text((390, 232), title, font=title_font, fill=(25, 42, 68))
    wrapped = textwrap.fill(subtitle, width=32)
    d.multiline_text((210, 410), wrapped, font=sub_font, fill=(73, 88, 110), spacing=18)

    hint = "이 이미지를 실제 학원 사진으로 교체하세요"
    bbox = d.textbbox((0, 0), hint, font=hint_font)
    tw = bbox[2] - bbox[0]
    tx = (w - tw) / 2
    d.rounded_rectangle((tx - 30, h - 250, tx + tw + 30, h - 178), radius=25, fill=(242, 246, 251))
    d.text((tx, h - 235), hint, font=hint_font, fill=(100, 115, 135))

    img.save(assets / filename, quality=92)
    print("saved", filename)


make_placeholder("hero.jpg", "아이의 가능성을 디자인하다", "ELS 영어수학학원의 교육 철학과 학습 시스템을 소개합니다.", accent=(28, 78, 121))
make_placeholder("director.jpg", "원장 소개", "20년 교육 현장의 경험을 바탕으로 학생의 성장 과정까지 설계합니다.", accent=(41, 112, 122))
make_placeholder("english-class.jpg", "영어 프로그램", "초등 파닉스부터 중·고등 내신과 수능 영어까지 단계별로 지도합니다.", accent=(53, 99, 233))
make_placeholder("math-class.jpg", "수학 프로그램", "개념 이해, 유형 적용, 오답 관리가 연결되는 학습을 설계합니다.", accent=(234, 142, 43))
make_placeholder("learning-system.jpg", "학습관리 시스템", "출결·과제·테스트·학습 리포트를 기록하여 학부모님과 공유합니다.", accent=(33, 151, 111))
make_placeholder("academy-space.jpg", "학원 공간과 수업 모습", "실제 교실, 수업, 개별 코칭 사진을 넣으면 신뢰도가 높아집니다.", accent=(121, 83, 197))
print("done")
