from code.background import Background


#!/usr/bin/python
# -*- coding: utf-8 -*-

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1':
                list_level=[]
                for i in range(5):
                    list_level.append(Background(f'level1{i}', (0, 0)))
                    list_level.append(Background(f'level1{i}', (575, 0)))

                return list_level