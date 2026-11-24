[![make.fun · u-suga-two-lines-to-your-past-self-f36c83ca](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Adnanhasim8/makefun-suga-pastself-20261125/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Adnanhasim8/makefun-suga-pastself-20261125/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

# Two Lines to Your Past Self

Entry for the make.fun competition
[u-suga-two-lines-to-your-past-self-f36c83ca](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca).

`main.py` (Python 3.13 standard library only, no network) writes exactly two
lines to `/output/entry.txt` — 157 characters in total. Line one warns the
past self about one specific moment: the night his brother says he's leaving,
and the warning is not to laugh but to ask where he's going. Line two says
why it mattered: he never comes back, and the joke is the last thing he ever
hears from him. One concrete moment, one clear cause and effect, and the
mystery — where he was going, and why — left unanswered.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

The program asserts before writing that the entry is exactly two lines,
1–280 characters in total, with each line a single non-empty sentence.
