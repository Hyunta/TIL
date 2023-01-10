package play.springbatch;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

public class PlayTest
{
    @ParameterizedTest
    @ValueSource(ints = {1, 25, 26, 109})
    @DisplayName("contents")
    void name(int n)
    {
        System.out.println(n / 10 * 10);
    }
}
