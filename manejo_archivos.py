#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

# registro={} #inicializar el tipo de dato que se va a usar

registro = {1:["AMANDA GIRALDO MUNEVAR",["PROGRAMACIÓN","INGLÉS","COUCHING"], True],
            2:["JORGE RODRIGUEZ ALANIS",["PROGRAMACIÓN","INGLÉS","COUCHING"], True],
            3:["JAVIER HERNANDEZ MORA", ["PROGRAMACIÓN","INGLÉS","COUCHING"], False],
            3:["JAVIER HERNANDEZ MORA", ["PROGRAMACIÓN","INGLÉS","COUCHING"], False]}

# registro[1] = ["AMANDA GIRALDO MUNEVAR",["PROGRAMACIÓN","INGLÉS","COUCHING"], True]
# registro[2] = ["JORGE RODRIGUEZ ALANIS",["PROGRAMACIÓN","INGLÉS","COUCHING"], True]
# registro[3] = ["JAVIER HERNANDEZ MORA", ["PROGRAMACIÓN","INGLÉS","COUCHING"], False]


objson = json.dumps(registro)


with open("alumnos.json", "w") as file:
      json.dump(objson, file, ensure_ascii=False, indent=4)