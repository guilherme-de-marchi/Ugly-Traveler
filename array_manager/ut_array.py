class UTArray:
    def __init__(self, array_to_convert: list, represents_availability: list, represents_unavailability: list) -> None:
        self.array = UTArray.array2UTArray(array_to_convert, represents_availability, represents_unavailability)
    
    @classmethod
    def array2UTArray(cls, array_to_convert: list, represents_availability: list, represents_unavailability: list):
        nodes_array = cls.elementsArray2UTArrayNode(
            array_to_convert,
            represents_availability,
            represents_unavailability,    
        )
        converted_array = cls.defineNodesNeighbors(nodes_array)

        return converted_array

    @classmethod
    def elementsArray2UTArrayNode(cls, array_to_convert: list, represents_availability: list, represents_unavailability: list):
        assert isinstance(array_to_convert, list)
        assert isinstance(represents_availability, list)
        assert isinstance(represents_unavailability, list)

        array = []

        for line in array_to_convert:
            array.append([])

            for element in line:
                if element in represents_unavailability:
                    array[-1].append(None)

                elif element in represents_availability:
                    array[-1].append(UTArrayNode())

                else:
                    raise ValueError('unknowed element')

        return array

    @classmethod
    def defineNodeByDirection(cls, nodes_array, base_element, base_element_position, direction) -> 'UTArrayNode':
        assert isinstance(base_element, UTArrayNode)

        directions = {
            'up': [-1, 0],
            'down': [1, 0],
            'left': [0, -1],
            'right': [0, 1],
        }

        y, x = base_element_position

        try:
            if y + directions[direction][0] >= 1 or x + directions[direction][1] >= 1:
                base_element.neighbors[direction] = nodes_array[y + directions[direction][0]][x + directions[direction][1]]

        except IndexError:
            pass

        return base_element

    @classmethod
    def defineNodesNeighbors(cls, nodes_array):
        for y in range(len(nodes_array)):
            for x in range(len(nodes_array[y])):
                for direction in ['up', 'down', 'left', 'right']:

                    element = nodes_array[y][x]

                    if element != None:
                        nodes_array[y][x] = cls.defineNodeByDirection(
                            nodes_array,
                            element,
                            (y, x),
                            direction,
                        )

        return nodes_array

class UTArrayNode:
    id = 0

    @classmethod
    def newId(cls) -> int:
        cls.id += 1
        return cls.id

    def __init__(self) -> None:
        self.id = UTArrayNode.newId()
        self.neighbors = {
            'up': None,
            'down': None,
            'left': None,
            'right': None,
        }