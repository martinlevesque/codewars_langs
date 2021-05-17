defmodule Bouncingball do

    defp bouncing_ball_count(h, bounce, window, cur_nb) do
        if h <= window do
            cur_nb-1
        else
            bouncing_ball_count(h*bounce, bounce, window, cur_nb+2)
        end
    end

    def bouncing_ball(h, bounce, window) do
        cond do
            h <= 0 -> -1
            not (bounce >= 0 and bounce < 1) -> -1
            window >= h -> -1
            true -> bouncing_ball_count(h, bounce, window, 0)
        end
    end

end
