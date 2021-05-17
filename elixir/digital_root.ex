defmodule Kata do
    def digital_root(n) do
        result = Integer.to_string(n)
        |> String.graphemes
        |> Enum.map(fn x -> String.to_integer(x) end)
        |> Enum.sum

        if result >= 10 do
            digital_root(result)
        else
            result
        end
    end
end

IO.puts Kata.digital_root(493193)