import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "skills" / "mindfluence" / "scripts"))

from anti_patterns import check  # noqa: E402

SAMPLES = {
    "ap01_vague_social_proof": ("AP-1", "Thousands of customers trust our platform every day. Join them."),
    "ap02_fear_no_exit": ("AP-2", "AI will replace your team within two years. The window is closing."),
    "ap03_framing_no_anchor": ("AP-3", "This isn't another project management tool. It's a new way to work."),
    "ap04_authority_no_proof": ("AP-4", "Studies show that teams using our method ship 3x faster."),
    "ap05_transactional_reciprocity": ("AP-5", "Here is a free checklist. Book a demo today and we will walk you through it."),
    "ap06_fake_scarcity": ("AP-6", "Only 3 seats left. The offer ends in 2 hours."),
    "ap07_premature_sunk_cost": ("AP-7", "You have already read this far. Do not waste the progress."),
    "ap08_empty_in_group": ("AP-8", "Join a community of like-minded people who care about growth."),
    "ap09_wrong_source_halo": ("AP-9", "As seen on Forbes and TechCrunch, trusted by industry leaders."),
    "ap10_insulting_confirmation": ("AP-10", "Most people are wrong about pricing. They keep discounting."),
    "ap11_abstract_availability": ("AP-11", "Imagine struggling with productivity. Picture a better workflow."),
    "ap12_blaming_dissonance": ("AP-12", "You say you care about quality, but you keep shipping bugs."),
    "ap13_statistical_only": ("AP-13", "The median graduate adds $27,400 in 90 days (N=214). 68% report a promotion."),
}

COMPLIANT = """[LANG: en]
Remote teams do not lose focus in meetings. They lose the two hours around them.
[illustrative] One platform team kept a shared doc for every decision. The rule was simple: if a decision needs a meeting, the meeting starts with a written proposal.
What does your team protect: the meeting, or the block of focus around it?"""


class AntiPatternTests(unittest.TestCase):
    def test_compliant_is_clean(self):
        self.assertEqual(check(COMPLIANT, "standard"), [])

    def test_each_sample_triggers_its_rule(self):
        for name, (expected, text) in SAMPLES.items():
            with self.subTest(name=name):
                ids = [f.id for f in check(text, "standard")]
                self.assertIn(expected, ids)

    def test_ap13_skipped_for_compact(self):
        _, text = SAMPLES["ap13_statistical_only"]
        ids = [f.id for f in check(text, "compact")]
        self.assertNotIn("AP-13", ids)

    def test_ap9_is_review_not_fail(self):
        _, text = SAMPLES["ap09_wrong_source_halo"]
        finding = next(f for f in check(text, "standard") if f.id == "AP-9")
        self.assertEqual(finding.severity, "review")

    def test_fear_needs_a_solution_in_the_same_paragraph(self):
        text = "AI will replace your team.\n\nHere is a guide to start."
        ids = [f.id for f in check(text, "standard")]
        self.assertIn("AP-2", ids)

    def test_gift_and_ask_in_separate_paragraphs_is_allowed(self):
        text = "Here is a free checklist.\n\nBook a demo when you are ready."
        ids = [f.id for f in check(text, "standard")]
        self.assertNotIn("AP-5", ids)


if __name__ == "__main__":
    unittest.main()
