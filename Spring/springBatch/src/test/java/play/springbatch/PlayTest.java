package play.springbatch;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.assertj.core.api.Assertions.assertThat;

public class PlayTest
{
    @ParameterizedTest
    @ValueSource(ints = {1, 25, 26, 109})
    @DisplayName("contents")
    void name(int n)
    {
        System.out.println(n / 10 * 10);
    }

    @Test
    @DisplayName("try-catch-finally 에서 catch 부분에서 exception을 던쟈도 finally가 작동한다.")
    void tryCatchFinally()
    {
        String value = "result";
        assertThat(checkTryCatch(value)).isEqualTo(value);
    }

    @Test
    @DisplayName("contents")
    void exceptionMessage()
    {
        try
        {
            throw new IllegalArgumentException("message");
        }
        catch (Exception e)
        {
            System.out.println(getMessage(e));
        }
    }

    private String getMessage(Exception e)
    {
        return e.getMessage();
    }

    private static String checkTryCatch(String value)
    {
        try
        {
            System.out.println("try 부분");
            throw new IllegalArgumentException();
        }
        catch (RuntimeException e)
        {
            System.out.println("runtimeException 부분");
            throw e;
        }
        catch (Exception e)
        {
            System.out.println("exception 부분");
            throw e;
        }
        finally
        {
            return value;
        }

    }
}
