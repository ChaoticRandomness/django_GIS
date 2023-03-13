import folium
from django.shortcuts import render


def map_view(request):
    # 取得兩個座標
    lat1 = request.GET.get('lat1', '')
    lng1 = request.GET.get('lng1', '')
    lat2 = request.GET.get('lat2', '')
    lng2 = request.GET.get('lng2', '')

    # 將座標轉換為浮點數
    lat1 = float(lat1) if lat1 else None
    lng1 = float(lng1) if lng1 else None
    lat2 = float(lat2) if lat2 else None
    lng2 = float(lng2) if lng2 else None

    # 建立地圖
    map_center = [25.5, 120]
    zoom_level = 6
    m = folium.Map(location=map_center, zoom_start=zoom_level)

    # 繪製兩個座標之間的線條
    if lat1 is not None and lng1 is not None and lat2 is not None and lng2 is not None:
        points = [[lat1, lng1], [lat2, lng2]]
        folium.PolyLine(points, color='red').add_to(m)

    # 將地圖轉換為 HTML 代碼
    map_html = m._repr_html_()

    # 傳遞地圖 HTML 代碼至模板
    context = {'map_html': map_html}
    return render(request, r'map_view.html', context)
