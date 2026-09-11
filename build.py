# -*- coding: utf-8 -*-
"""Build the whole site: every language, then the shared post-processing.

    python3 build.py

Generators only write plain pages. The switcher, hreflang, Open Graph tags,
typography, cache-busting and the sitemap are applied afterwards by l10n.py,
so adding a language means adding a gen_*.py and one line below.
"""
import gen                                    # noqa: F401  (writes JA)
import gen_en                                 # noqa: F401  (writes EN)
import gen_fr                                 # noqa: F401  (writes FR)
import gen_zh                                 # noqa: F401  (writes ZH-Hant)
import l10n

l10n.finish({
    "":    gen_en.PAGES_JA_EN,
    "en/": gen_en.PAGES_JA_EN,
    "fr/": gen_fr.PAGES_FR,
    "zh/": gen_zh.PAGES_ZH,
})
print("build complete")
