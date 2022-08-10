public class PowerMod {
    static int exponentiation(int x, int y, int n)
    {
        int result = 1;
        x = x % n;
        while (y > 0)
        {
            if((y & 1)==1)
                result = (result * x) % n;
            y = y >> 1;
            x = (x * x) % n;
        }
        return result;
    }
