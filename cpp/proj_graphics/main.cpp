#include <cmath>
#define _USE_MATH_DEFINES
#include "CImg.h"

using namespace cimg_library;

using byte_t = unsigned char;
using color_t = byte_t[4];

color_t bialy = {255, 255, 255};
color_t bg_col = {18, 78, 135};
color_t niebieski = {86, 142, 200};
color_t ciemny_niebieski = {0, 68, 130};
color_t swietly_niebieski = {85, 144, 201};
color_t brack_col = {0, 89, 156};
size_t width = 1024;
size_t height = 720;
const int rozstawPlusa = 60;
const int gruboscPlusa = 10;

struct vec_t {
    int x, y;
};

int main() {
    CImg<byte_t> zdjecie(width, height, 1, 3, 255);
    zdjecie.draw_rectangle(0, 0, width, height, bg_col);

    vec_t wierzcholki[6];
    int cx = width/2, cy = height/2;
    int rad = 180;

    for (int i = 0; i < 6; i++) {
        float ang = 2*M_PI * i/6 + M_PI/6;
        wierzcholki[i].x = (int)(cx + rad * cos(ang));
        wierzcholki[i].y = (int)(cy + rad * sin(ang));
    }

    for (int i = 0; i < 2; i++) {
        int nast = (i + 1) % 6;
        zdjecie.draw_triangle(cx, cy, wierzcholki[i].x, wierzcholki[i].y, wierzcholki[nast].x, wierzcholki[nast].y, ciemny_niebieski);
    }

    for (int i = 2; i < 2; i++) {
        int nast = (i + 1) % 6;
        zdjecie.draw_triangle(cx, cy, wierzcholki[i].x, wierzcholki[i].y, wierzcholki[nast].x, wierzcholki[nast].y, niebieski);
    }

    for (int i = 4; i < 6; i++) {
        int nast = (i + 1) % 6;
        if (i == 5) {
            zdjecie.draw_triangle(cx, cy, wierzcholki[i].x, wierzcholki[i].y, wierzcholki[nast].x, wierzcholki[nast].y, brack_col);
            continue;
        }
        zdjecie.draw_triangle(cx, cy,
            wierzcholki[i].x, wierzcholki[i].y,
            wierzcholki[nast].x, wierzcholki[nast].y,
            niebieski);
    }

    int lbx = (wierzcholki[2].x - 160);
    int lby = cy;
    int lbs1x = (wierzcholki[2].x - 40);
    int lbs1y = cy - 160;
    int lbs2x = (wierzcholki[2].x - 40);
    int lbs2y = cy + 160;
    zdjecie.draw_triangle(lbx, lby, lbs1x, lbs1y, lbs2x, lbs2y, swietly_niebieski);
    zdjecie.draw_triangle(lbx + 35, lby, lbs1x, lbs1y + 40, lbs2x, lbs2y - 40, bg_col);

    int rtx = (wierzcholki[5].x + 160);
    int rty = cy;
    int rbs1x = (wierzcholki[5].x + 40);
    int rbs1y = cy - 160;
    int rbs2x = (wierzcholki[5].x + 40);
    int rbs2y = cy + 160;
    zdjecie.draw_triangle(rtx, rty, rbs1x, rbs1y, rbs2x, rbs2y, swietly_niebieski);
    zdjecie.draw_triangle(rtx - 35, rty, rbs1x, rbs1y + 40, rbs2x, rbs2y - 40, bg_col);


    int tr_x = wierzcholki[5].x + 120;
    int tr_y = wierzcholki[5].y - 120;
    zdjecie.draw_circle(tr_x, tr_y, 28, swietly_niebieski);
    int bl_x = wierzcholki[2].x - 120;
    int bl_y = wierzcholki[2].y + 120;
    zdjecie.draw_circle(bl_x, bl_y, 20, swietly_niebieski);
    int wewnetrznyC = 40, zewnetrznyC = 70;

    int centrCx = cx - 10;
    int centrCy = cy;
    int outer_radius = 90;
    int grubosc = 25;

    for (double ang = 45; ang <= 315; ang += 0.5) {
        double rad = ang * M_PI / 180.0;
        for (int r = outer_radius - grubosc; r <= outer_radius; ++r) {
            int x, y;
            x = (centrCx + r * cos(rad));
            y = (centrCy + r * sin(rad));
            zdjecie.draw_point(x, y, bialy);
        }
    }

    int rozmiarPlusa = 20;

    int centrPierwPlusaX = (cx - 80) + zewnetrznyC + 75;
    int centrPierwPlusaY = cy;
    
    for (int off = -gruboscPlusa / 2; off <= gruboscPlusa / 2; off++) {
        zdjecie.draw_line(centrPierwPlusaX - rozmiarPlusa, centrPierwPlusaY + off, centrPierwPlusaX + rozmiarPlusa, centrPierwPlusaY + off, bialy);
    }

    for (int off = -gruboscPlusa / 2; off <= gruboscPlusa / 2; off++) {
        zdjecie.draw_line(centrPierwPlusaX + off, centrPierwPlusaY - rozmiarPlusa, centrPierwPlusaX + off, centrPierwPlusaY + rozmiarPlusa, bialy);
    }

    int centrDrugPlusaX = centrPierwPlusaX + rozstawPlusa;
    int centrDrugPlusaY = centrPierwPlusaY;
    
    for (int off = -gruboscPlusa / 2; off <= gruboscPlusa / 2; off++) {
        zdjecie.draw_line(centrDrugPlusaX - rozmiarPlusa, centrDrugPlusaY + off, centrDrugPlusaX + rozmiarPlusa, centrDrugPlusaY + off, bialy);
    }
    
    for (int off = -gruboscPlusa / 2; off <= gruboscPlusa / 2; off++) {
        zdjecie.draw_line(centrDrugPlusaX + off, centrDrugPlusaY - rozmiarPlusa, centrDrugPlusaX + off, centrDrugPlusaY + rozmiarPlusa, bialy);
    }

    CImgDisplay wysw(zdjecie, "CPP");
    while (!wysw.is_closed()) {
        wysw.wait();
    }
    
    zdjecie.save("logo.bmp");

    return 0;
}