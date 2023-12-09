# matplot-templates

Styled plot scripts with `matplotlib`.

Tips may save your time:
1. For each figure in the paper, create a script for plotting
   - name the file `<sec#>-<figname>.py`, e.g. `6-eval-compare-baseline.py`
2. Organize each script in three parts: style, data, plot


**Table of Examples**
| Figure Type     | Script                                                                | Demo                                                                                        |
| --------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Bar             | [5-bar-running-time.py](./examples/5-bar-running-time.py)             | ![](examples/figures/5-running-time.svg)                                                    |
| Multi-bars      | [5-multibars-running-time.py](./examples/5-multibars-running-time.py) | ![](examples/figures/5-multibars-running-time.svg)                                          |
| CDF             | [1-config-change-cdf.py](./examples/1-config-change-cdf.py)           | ![1-config-change-cdf.svg](examples/figures/1-config-change-cdf.svg)                        |
| horizontal bar  | [6-eval-survey.py](./examples/6-eval-survey.py)                       | ![6-eval-survey.svg](examples/figures/6-eval-survey.svg)                                    |
| Bar and line    | [6-overhead.py](./examples/6-overhead.py)                             | ![6-overhead.svg](examples/figures/6-overhead.svg)                                          |
| Autocorrelation | [6-relative-risk.py](./examples/6-relative-risk.py)                   | ![6-risk-order-by-test-duration-2.sv](examples/figures/6-risk-order-by-test-duration-2.svg) |
| Stacked bars    | [6-fig13-computing-time.py](./examples/6-fig13-computing-time.py)     | ![6-fig13-computing-time.svg](examples/figures/6-fig13-computing-time.svg)                  |
| Histogram       | [6-multichange.py](./examples/6-multichange.py)                       | ![6-histo-multichange.svg](examples/figures/6-histo-multichange.svg)                        |
