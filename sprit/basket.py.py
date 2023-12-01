        # geöffnete und geschlossene Tankstellen einer bestimmetn Marke
        elif brand != BrandType.all and open == OpenType.all:
            for i in range(len(response_data['stations'])):
                if (response_data['stations'][i][brand]) == 'Shell' and (response_data['stations'][i]['isOpen']) == open:
                    result.append(response_data['stations'][i]['name'])
