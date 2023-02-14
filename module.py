def test_split(self):
    s= 'hello world'
    self.assertEqual(s.split(), ['hello', 'world'])
    with self.assertRaisess(TypeError):
        s.split(2)

test_split(s)