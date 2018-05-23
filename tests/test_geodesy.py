import unittest
from conversions import dms2dd, dd2dms
from geodesy import vincinv, vincdir

class TestGeodesy(unittest.TestCase):
    def test_vincinv(self):
        # Flinders Peak
        lat1 = dms2dd(-37.57037203)
        long1 = dms2dd(144.25295244)

        # Buninyong
        lat2 = dms2dd(-37.39101561)
        long2 = dms2dd(143.55353839)

        ell_dist, azimuth1to2, azimuth2to1 = vincinv(lat1, long1, lat2, long2)
        self.assertEqual(round(ell_dist, 3), 54972.271)
        self.assertEqual(round(dd2dms(azimuth1to2), 6), 306.520537)
        self.assertEqual(round(dd2dms(azimuth2to1), 6), 127.102507)

    def test_vincdir(self):
        # Flinders Peak
        lat1 = dms2dd(-37.57037203)
        long1 = dms2dd(144.25295244)

        # To Buninyong
        azimuth1to2 = dms2dd(306.520537)
        ell_dist = 54972.271

        lat2, long2, azimuth2to1 = vincdir(lat1, long1, azimuth1to2, ell_dist)
        self.assertEqual(round(dd2dms(lat2), 8), -37.39101562)
        self.assertEqual(round(dd2dms(long2), 8), 143.55353840)
        self.assertEqual(round(dd2dms(azimuth2to1), 6), 127.102507)



if __name__ == '__main__':
    unittest.main()
