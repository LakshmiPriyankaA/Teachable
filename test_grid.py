from grid import NeighboringNodes
from enum import Enum , auto,unique
@unique           
class NeighborhoodType(Enum):
    CROSS = auto()
    DIAMOND = auto()
    SQUARE = auto()

def test_initialvalue():
    pass

def test_topological_nodes():
    params=[1,1,1]
    nn=NeighboringNodes(3,True)
    pass
 
    nds=nn.topological_nodes(*params,type=NeighborhoodType.DIAMOND)
    print(nds)
    assert nds==[(0,1),(1,0),(1,1),(1,2),(2,1)]
    nds=nn.topological_nodes(*params,type=NeighborhoodType.CROSS)
    print(nds)
    assert nds==[(0,1),(1,0),(1,1),(1,2),(2,1)]



