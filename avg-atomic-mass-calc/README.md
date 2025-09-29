# Average Atomic Mass Calculator

This is a super basic calculator (written in python) used to calculate the average atomic mass from isotopes of an element. I made it for my chemistry class.

**Best use is to upload it to a TI-84 CE Plus Python if you have one and you can use it there an an aplication. Very useful**

## Function:

It works by allowing the user to input the number of isotopes to calculate, then the user inputs the abundance (in percent form) and the mass (in amu). The program then executes the formula below on those inputs for each isotope:

$$ (abundance / 100) * mass $$

After all atomic masses have been calculated, they are summed together to get the final average atomic mass.

### Example:

| Isotope | Abundance (%) | Mass (amu) |
|---------|---------------|------------|
| Mg-24 | 79.99% | 23.99 amu |
| Mg-25 | 10.00% | 24.99 amu |
| Mg-26 | 10.01% | 25.98 amu |

$$ 19.1896 = 79.99 * 23.99 $$
$$ 2.4990 = 10.00 * 24.99 $$
$$ 2.6006 = 10.01 * 25.98 $$

$$ 19.1896 + 2.4990 + 2.6006 = 24.2892 $$

**Average Atomic Mass: 24.2892 amu**
