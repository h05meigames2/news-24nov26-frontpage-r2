"""Front-page generator for the 24 November 2026 world-news image.

Draws a deterministic 1024x1024 newspaper front page with PIL only:
no network calls, no downloaded assets, no randomness. Every run
produces the same image from the same headlines baked in below.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

INK = (18, 18, 18)
PAPER = (247, 243, 232)
RED = (178, 34, 34)
NAVY = (24, 48, 88)
GREY = (96, 96, 96)
LIGHT = (226, 220, 205)
GOLD = (176, 132, 32)

HEADLINES = [
    ("LEAD", "FACTORY FIRE KILLS 24 IN INDONESIA",
     "A blaze at a candy factory in Banten leaves at least 24 dead "
     "and around 30 workers missing as rescuers search the ruins."),
    ("WAR IN EUROPE", "KYIV REGION HIT AS WAR SPREADS",
     "Russian drone and missile strikes kill people in Ukraine's "
     "Kyiv region. A Russian cargo ship burns in the Gulf of "
     "Finland after a drone attack, and a Russian corvette is "
     "reported destroyed in the Libyan port of Benghazi."),
    ("CLIMATE", "COP31 ENDS WITHOUT FOSSIL-FUEL DEAL",
     "Climate talks in Antalya, Turkiye, close divided over "
     "fossil-fuel language, drawing criticism from several nations."),
    ("EUROPE", "LISBON MARCHES OVER COST OF LIVING",
     "Thousands take to the streets of Portugal's capital to "
     "protest rising prices."),
    ("DIPLOMACY", "INDIA AND NEPAL OPEN NEW RAIL LINK",
     "PM Modi and Nepal PM Balendra Shah flag off the "
     "Saryu-Kamala Express, linking Ayodhya and Janakpur Dham."),
    ("SPORT", "ALCARAZ TAKES ATP FINALS CROWN",
     "Carlos Alcaraz beats Alexander Zverev in Turin. Max "
     "Verstappen wins the Las Vegas Grand Prix, and Rishabh Pant "
     "hits 128 for India in Wellington."),
]

FOOTER_ITEMS = [
    "Trump's outreach to Kim Jong Un goes unanswered",
    "Nvidia rallies as Jensen Huang returns",
    "World Chess Championship begins in Geneva",
]


def _font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def _rule(draw, y, color=INK, width=2):
    draw.line([(48, y), (W - 48, y)], fill=color, width=width)


def _story(draw, x, y, w, tag, title, body, title_size=34):
    draw.rectangle([x, y, x + 150, y + 26], fill=RED)
    draw.text((x + 8, y + 4), tag, font=_font(15, bold=True),
              fill=(255, 255, 255))
    y += 38
    for line in _wrap(draw, title, _font(title_size, bold=True), w):
        draw.text((x, y), line, font=_font(title_size, bold=True), fill=INK)
        y += title_size + 6
    y += 4
    for line in _wrap(draw, body, _font(19), w):
        draw.text((x, y), line, font=_font(19), fill=(52, 52, 52))
        y += 26
    return y


def build(path):
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # Masthead
    draw.text((48, 26), "THE WORLD", font=_font(88, bold=True), fill=NAVY)
    draw.text((48, 122), "TUESDAY 24 NOVEMBER 2026  |  ONE DAY, ONE IMAGE",
              font=_font(21, bold=True), fill=RED)
    _rule(draw, 158, width=4)
    _rule(draw, 166, width=1)

    # Lead story, full width, with a red-tinted photo-style panel
    draw.rectangle([48, 182, 976, 330], fill=(214, 88, 66))
    draw.rectangle([48, 182, 976, 330], outline=INK, width=3)
    draw.text((72, 212), "BANTEN, INDONESIA", font=_font(24, bold=True),
              fill=(255, 255, 255))
    draw.text((72, 248), "SMOKE OVER THE", font=_font(34, bold=True),
              fill=(255, 255, 255))
    draw.text((72, 286), "FACTORY FLOOR", font=_font(34, bold=True),
              fill=(255, 255, 255))
    y = _story(draw, 48, 352, 928, HEADLINES[0][0], HEADLINES[0][1],
               HEADLINES[0][2], title_size=40)
    _rule(draw, y + 14)

    # Two-column middle stories, both starting at the same baseline
    col_top = y + 34
    y = _story(draw, 48, col_top, 440, HEADLINES[1][0], HEADLINES[1][1],
               HEADLINES[1][2], title_size=30)
    y2 = _story(draw, 536, col_top, 440,
                HEADLINES[2][0], HEADLINES[2][1], HEADLINES[2][2],
                title_size=30)
    mid = max(y, y2)
    _rule(draw, mid + 14)

    # Bottom row: three short stories side by side
    y = mid + 34
    col_w, gap = 288, 32
    for i, (tag, title, body) in enumerate(HEADLINES[3:]):
        x = 48 + i * (col_w + gap)
        draw.rectangle([x, y, x + 120, y + 24], fill=NAVY)
        draw.text((x + 7, y + 3), tag, font=_font(14, bold=True),
                  fill=(255, 255, 255))
        yy = y + 34
        for line in _wrap(draw, title, _font(21, bold=True), col_w):
            draw.text((x, yy), line, font=_font(21, bold=True), fill=INK)
            yy += 27
        yy += 4
        for line in _wrap(draw, body, _font(16), col_w):
            draw.text((x, yy), line, font=_font(16), fill=(52, 52, 52))
            yy += 22

    # Footer strip
    fy = H - 78
    draw.rectangle([0, fy, W, H], fill=NAVY)
    draw.text((48, fy + 12), "ALSO TODAY", font=_font(17, bold=True),
              fill=GOLD)
    draw.text((48, fy + 38), "  |  ".join(FOOTER_ITEMS), font=_font(15),
              fill=(255, 255, 255))
    img.save(path)
    return path


if __name__ == "__main__":
    build("/output/entry.png")
    print("wrote /output/entry.png")
