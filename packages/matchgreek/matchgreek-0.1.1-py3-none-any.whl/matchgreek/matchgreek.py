#    matchgreek is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    matchgreek is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with matchgreek.  If not, see <https://www.gnu.org/licenses/>.

print("matchgreek v.0.1")
import re
import sys

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path)

    p = parser.parse_args()

    if p.file_path.exists():
        filename = p.file_path
    else:
        raise ValueError("no such file")


    with open(str(filename), 'r') as myfile:
      texcontent = myfile.read()

    greek_letters =  { "uc_gamma":{"symbol":"Γ", "tex":"\\\\Gamma"},
                         "uc_delta":{"symbol":"Δ", "tex":"\\\\Delta"},
                         "uc_lambda":{"symbol":"Λ","tex":"\\\\Lambda"},
                         "uc_phi"  :{"symbol":"Φ", "tex":"\\\\Phi"},
                         "uc_pi"   :{"symbol":"Π", "tex":"\\\\Pi"},
                         "uc_psi"  :{"symbol":"Ψ", "tex":"\\\\Psi"},
                         "uc_sigma":{"symbol":"Σ", "tex":"\\\\Sigma"},
                         "uc_theta":{"symbol":"Θ", "tex":"\\\\Theta"},
                         "uc_upsilon":{"symbol":"s", "tex":"\\\\Upsilon"},
                         "uc_xi"   :{"symbol":"Ξ", "tex":"\\\\Xi"},
                         "uc_omega":{"symbol":"Ω", "tex":"\\\\Omega"},
                         "lc_alpha":{"symbol":"α", "tex":"\\\\alpha"},
                         "lc_beta":{"symbol":"β", "tex":"\\\\beta"},
                         "lc_gamma":{"symbol":"γ", "tex":"\\\\gamma"},
                         "lc_delta":{"symbol":"δ", "tex":"\\\\delta"},
                         "lc_epsilon":{"symbol":"ϵ", "tex":"\\\\epsilon"},
                         "lc_zeta":{"symbol":"ζ", "tex":"\\\\zeta"},
                         "lc_eta":{"symbol":"η", "tex":"\\\\eta"},
                         "lc_theta":{"symbol":"θ", "tex":"\\\\theta"},
                         "lc_iota":{"symbol":"ι" ,"tex":"\\\\iota"},
                         "lc_kappa":{"symbol":"κ" ,"tex":"\\\\kappa"},
                         "lc_lambda":{"symbol":"λ" ,"tex":"\\\\lambda"},
                         "lc_mu":{"symbol":"μ" ,"tex":"\\\\mu"},
                         "lc_nu":{"symbol":"ν" ,"tex":"\\\\nu"},
                         "lc_xi":{"symbol":"ξ" ,"tex":"\\\\xi"},
                         "lc_pi":{"symbol":"π" ,"tex":"\\\\pi"},
                         "lc_rho":{"symbol":"ρ" ,"tex":"\\\\rho"},
                         "lc_sigma":{"symbol":"σ" ,"tex":"\\\\sigma"},
                         "lc_tau":{"symbol":"τ" ,"tex":"\\\\tau"},
                         "lc_upsilon":{"symbol":"υ" ,"tex":"\\\\upsilon"},
                         "lc_phi":{"symbol":"ϕ" ,"tex":"\\\\phi"},
                         "lc_chi":{"symbol":"χ" ,"tex":"\\\\chi"},
                         "lc_psi":{"symbol":"ψ" ,"tex":"\\\\psi"},
                         "lc_omega":{"symbol":"ω" ,"tex":"\\\\omega"},
                         "digamma":{"symbol":"ϝ", "tex":"\\\\digamma"},
                         "varepsil":{"symbol":"ε", "tex":"\\\\varepsilon"},
                         "varkappa":{"symbol":"ϰ", "tex":"\\\\varkappa"},
                         "varphi":{"symbol":"φ", "tex":"\\\\varphi"},
                         "varpi":{"symbol":"ϖ", "tex":"\\\\varpi"},
                         "varrho":{"symbol":"ϱ", "tex":"\\\\varrho"},
                         "varsigma":{"symbol":"ς", "tex":"\\\\varsigma"},
                         "vartheta":{"symbol":"ϑ", "tex":"\\\\vartheta"},
    }


    used_letters = set()
    for k,v in greek_letters.items():
        if re.findall(v['tex'], texcontent):
            used_letters.add(k)

    unused_letters = set(greek_letters.keys()) - used_letters

    print("=" * 5 + "Used Letters" + "=" * 5)

    for l in used_letters:
        print(greek_letters[l]["symbol"] + "   "  + greek_letters[l]["tex"][1:])

    print("\n" * 2)

    print("=" * 5 + "Unused Letters" + "=" * 5)

    for l in unused_letters:
        print(greek_letters[l]["symbol"] + "   "  + greek_letters[l]["tex"][1:])


if __name__ == "__main__":
    main()
