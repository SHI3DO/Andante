import glob
import os
import json


def get():
    target = os.path.join("./maps/**", "*json")
    tmpd = glob.glob(target)
    clist = []
    for i in range(0, len(tmpd)):
        clist.append([tmpd[i]])

    for i in range(0, len(clist)):
        with open(clist[i][0], 'r', encoding='UTF-8') as f:
            data = json.load(f)
            clist[i].append(json.dumps(data['title'], ensure_ascii=False))
            clist[i].append(json.dumps(data['writer'], ensure_ascii=False))
            clist[i].append(json.dumps(data['creator'], ensure_ascii=False))
    print(clist)
    return clist


def draw(screen, pg, screenx, screeny, maplist, BoldFont, LightFont):
    for mapnum in range(0, len(maplist)):
        container = pg.Surface((screenx / 2.3, screeny / 6))
        container.set_alpha(120 * (1 / (mapnum + 1) ** 0.5))
        container.fill((0, 0, 0))
        screen.blit(container, (1 + screenx - screenx / 2.3, screeny / 8 + (screeny / 98 + screeny / 6) * mapnum))
        title = BoldFont.render(maplist[mapnum][1], True, (255, 255, 255))
        screen.blit(title, (10 + screenx - screenx / 2.3, screeny / 8 + (screeny / 98 + screeny / 6) * mapnum))
        writer = LightFont.render("by " + maplist[mapnum][2], True, (255, 255, 255))
        screen.blit(writer, (title.get_width() + 20 + screenx - screenx / 2.3,
                             title.get_height() / 4 + screeny / 8 + (screeny / 98 + screeny / 6) * mapnum))
