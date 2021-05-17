
defmodule Kata do
    def matrix_addition([head1|tail1], [head2|tail2]) do
        [head1|tail1]
        |> Enum.with_index
        |> Enum.map(fn {elem, index}->
            matrix_addition(elem, Enum.at([head2|tail2], index))
        end)
    end

    def matrix_addition(elem1, elem2) do
        elem1 + elem2
    end
end
