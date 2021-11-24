import folium
map = folium.Map(location=[-19.932452, -43.937944],
                 titles='Stamen Terrain',
                 zoom_start=16)

folium.Marker(
    [-19.932452, -43.937944],
    popup='<i>Praça da Liberdade</i>',
    tooltip='Clique aqui'
).add_to(map)

map.save('CAMINHO PARA SALVAR O ARQUIVO .html')