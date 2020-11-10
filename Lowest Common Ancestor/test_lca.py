import unittest
import lca

class Testlca(unittest.TestCase):

    def test_getlca(self):
        f = lca.node('F', None)
        a = lca.node('A', f)
        c = lca.node('C', f)
        h = lca.node('H', a)
        e = lca.node('E', a)
        i = lca.node('I', c)
        b = lca.node('B', e)
        t = lca.node('T', e)
        d = lca.node('D', i)
        self.assertEqual('A', lca.getlca(h, t))
        self.assertEqual('F', lca.getlca(h, t))
        self.assertEqual('F', lca.getlca(h, t))
        self.assertEqual('E', lca.getlca(h, t))
        self.assertEqual('none', lca.getlca(h, t))
    
    