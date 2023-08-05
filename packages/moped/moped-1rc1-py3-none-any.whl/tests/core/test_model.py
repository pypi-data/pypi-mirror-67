import unittest
import numpy as np

from moped import Compound, Reaction, Model


class ModelTests(unittest.TestCase):
    def test_add_compound(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        self.assertEqual(tuple(m.compounds.keys()), ("cpd1_c",))

    def test_compound_independence(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        compound = Compound(base_id="cpd1", compartment="CYTOSOL")
        m1 = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m2 = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m1.add_compound(compound)
        m2.add_compound(compound)
        m2.compounds["cpd1_c"].in_reaction.add("rxn1_c")
        self.assertEqual(m1.compounds["cpd1_c"].in_reaction, set())
        self.assertEqual(m2.compounds["cpd1_c"].in_reaction, {"rxn1_c"})

    def test_add_compound_nonsense_input_str(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        with self.assertRaises(TypeError):
            m.add_compound("cpd")

    def test_add_compound_nonsense_input_int(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        with self.assertRaises(TypeError):
            m.add_compound(1)

    def test_add_compound_nonsense_input_float(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        with self.assertRaises(TypeError):
            m.add_compound(1.0)

    def test_add_compound_nonsense_input_none(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        with self.assertRaises(TypeError):
            m.add_compound(None)

    def test_add_compound_nonsense_input_list(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        cpd1 = Compound(base_id="cpd1", compartment="CYTOSOL")
        with self.assertRaises(TypeError):
            m.add_compound([cpd1])

    def test_add_compound_nonsense_input_set(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        cpd1 = Compound(base_id="cpd1", compartment="CYTOSOL")
        with self.assertRaises(TypeError):
            m.add_compound({cpd1})

    def test_add_compound_nonsense_input_dict(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        cpd1 = Compound(base_id="cpd1", compartment="CYTOSOL")
        with self.assertRaises(TypeError):
            m.add_compound({"key": cpd1})

    def test_add_compound_nonsense_input_dict2(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        cpd1 = Compound(base_id="cpd1", compartment="CYTOSOL")
        with self.assertRaises(TypeError):
            m.add_compound({cpd1: "value"})

    def test_add_compounds(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        self.assertEqual(tuple(m.compounds.keys()), ("cpd1_c", "cpd2_c"))

    def test_add_compartment_compound_variant_extracellular(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        m.add_compartment_compound_variant("cpd1_c", "EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds.keys()), ("cpd1_c", "cpd1_e"))
        self.assertEqual(m.compounds["cpd1_c"].compartment, "CYTOSOL")
        self.assertEqual(m.compounds["cpd1_e"].compartment, "EXTRACELLULAR")

    def test_add_compartment_compound_variant_in_reaction(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reaction(
            Reaction(
                id="rxn1_c", base_id="rxn1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}
            )
        )
        m.add_compartment_compound_variant("cpd1_c", "EXTRACELLULAR")
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, set(["rxn1_c"]))
        self.assertEqual(m.compounds["cpd1_e"].in_reaction, set())

    def test_add_compartment_compound_missing_compound(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        with self.assertRaises(KeyError):
            m.add_compartment_compound_variant("cpd1_c", "EXTRACELLULAR")

    def test_set_compound_property(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        cpd1 = Compound(base_id="cpd1", compartment="CYTOSOL")
        m.add_compound(cpd1)
        m.set_compound_property(
            "cpd1_c",
            {
                "id": "cpd1_c",
                "name": "cpd2_c",
                "formula": {"C": 1, "H": 4},
                "charge": 5,
                "gibbs0": 4,
                "compartment": "_p",
                "smiles": "CH4",
                "types": ["Some type"],
                "in_reaction": ["rxn1_c"],
            },
        )
        self.assertEqual(m.compounds["cpd1_c"].id, "cpd1_c")
        self.assertEqual(m.compounds["cpd1_c"].name, "cpd2_c")
        self.assertEqual(m.compounds["cpd1_c"].formula, {"C": 1, "H": 4})
        self.assertEqual(m.compounds["cpd1_c"].charge, 5)
        self.assertEqual(m.compounds["cpd1_c"].gibbs0, 4)
        self.assertEqual(m.compounds["cpd1_c"].compartment, "_p")
        self.assertEqual(m.compounds["cpd1_c"].smiles, "CH4")
        self.assertEqual(m.compounds["cpd1_c"].types, ["Some type"])
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, ["rxn1_c"])

    def test_set_compound_property_wrong_key(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        cpd1 = Compound(base_id="cpd1", compartment="CYTOSOL")
        m.add_compound(cpd1)
        with self.assertRaises(KeyError):
            m.set_compound_property("cpd1_c", {"bogus-key": "bogus-value"})

    def test_remove_compound(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.remove_compound("cpd1_c")
        self.assertEqual(tuple(m.compounds.keys()), ("cpd2_c",))

    def test_remove_compounds_tuple(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            )
        )
        m.remove_compounds(("cpd1_c", "cpd3_c"))
        self.assertEqual(tuple(m.compounds.keys()), ("cpd2_c",))

    def test_remove_compounds_list(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            )
        )
        m.remove_compounds(["cpd1_c", "cpd3_c"])
        self.assertEqual(tuple(m.compounds.keys()), ("cpd2_c",))

    def test_remove_compounds_set(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            )
        )
        m.remove_compounds({"cpd1_c", "cpd3_c"})
        self.assertEqual(tuple(m.compounds.keys()), ("cpd2_c",))

    def test_remove_compounds_dict(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            )
        )
        m.remove_compounds({"cpd1_c": 1, "cpd3_c": 1})
        self.assertEqual(tuple(m.compounds.keys()), ("cpd2_c",))

    def test_remove_nonexistant_compound(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        with self.assertRaises(KeyError):
            m.remove_compound("cpd3")

    def test_get_reactions_of_compound(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        v1 = Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1})
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reaction(v1)
        self.assertEqual(m.get_reactions_of_compound("cpd1_c"), set(["v1"]))
        self.assertEqual(m.get_reactions_of_compound("cpd2_c"), set(["v1"]))

    def test_get_compounds_of_compartment(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m.add_compounds(
            (
                Compound(base_id="cpd0", compartment="CYTOSOL"),
                Compound(base_id="cpd1", compartment="PERIPLASM"),
                Compound(base_id="cpd2", compartment="EXTRACELLULAR"),
            )
        )
        self.assertEqual(m.get_compounds_of_compartment("CYTOSOL"), ["cpd0_c"])
        self.assertEqual(m.get_compounds_of_compartment("PERIPLASM"), ["cpd1_p"])
        self.assertEqual(m.get_compounds_of_compartment("EXTRACELLULAR"), ["cpd2_e"])

    def test_add_reaction(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reaction(Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}))
        self.assertEqual(tuple(m.reactions.keys()), ("v1",))
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, {"v1"})
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, {"v1"})

    def test_add_reaction_var(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reaction(
            Reaction(
                id="v1__var__0_c",
                base_id="v1",
                stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
            )
        )
        self.assertEqual(set(m.reactions.keys()), {"v1__var__0_c"})
        self.assertEqual(m.variant_reactions["v1"], {"v1__var__0_c"})
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, {"v1__var__0_c"})
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, {"v1__var__0_c"})

    def test_set_reaction_property(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reaction(Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}))
        m.set_reaction_property(
            "v1",
            {
                "id": "v1",
                "name": "v1",
                "stoichiometries": {"cpd1_c": 1, "cpd2_c": -1},
                "bounds": (-1000, 1000),
                "reversible": True,
                "gibbs0": 5,
                "ec": "5.4.123.2",
                "pathways": ["pwy-101"],
            },
        )
        self.assertEqual(m.reactions["v1"].id, "v1")
        self.assertEqual(m.reactions["v1"].name, "v1")
        self.assertEqual(m.reactions["v1"].stoichiometries, {"cpd1_c": 1, "cpd2_c": -1})
        self.assertEqual(m.reactions["v1"].bounds, (-1000, 1000))
        self.assertEqual(m.reactions["v1"].reversible, True)
        self.assertEqual(m.reactions["v1"].gibbs0, 5)
        self.assertEqual(m.reactions["v1"].ec, "5.4.123.2")
        self.assertEqual(m.reactions["v1"].pathways, ["pwy-101"])

    def test_set_reaction_property_wrong_key(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reaction(Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}))
        with self.assertRaises(KeyError):
            m.set_reaction_property("v1", {"bogus-key": "bogus-value"})

    def test_remove_reaction(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(id="v2", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
            )
        )
        m.remove_reaction("v1")
        self.assertEqual(tuple(m.reactions.keys()), ("v2",))

    def test_remove_reaction_var(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    pathways={"PWY101"},
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    pathways={"PWY101"},
                ),
            )
        )
        self.assertEqual(m.pathways["PWY101"], {"rxn1__var__1_c", "rxn1__var__0_c"})
        self.assertEqual(
            m.variant_reactions["rxn1"], {"rxn1__var__1_c", "rxn1__var__0_c"}
        )
        self.assertEqual(
            m.compounds["cpd1_c"].in_reaction, {"rxn1__var__1_c", "rxn1__var__0_c"}
        )
        self.assertEqual(
            m.compounds["cpd2_c"].in_reaction, {"rxn1__var__1_c", "rxn1__var__0_c"}
        )

        m.remove_reaction("rxn1__var__0_c")
        self.assertEqual(m.pathways["PWY101"], {"rxn1__var__1_c"})
        self.assertEqual(m.variant_reactions["rxn1"], {"rxn1__var__1_c"})
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, {"rxn1__var__1_c"})
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, {"rxn1__var__1_c"})

        m.remove_reaction("rxn1__var__1_c")
        with self.assertRaises(KeyError):
            m.pathways["PWY101"]
        with self.assertRaises(KeyError):
            m.variant_reactions["rxn1"]
        with self.assertRaises(KeyError):
            m.compounds["cpd1_c"]
        with self.assertRaises(KeyError):
            m.compounds["cpd2_c"]

    def test_remove_reaction_compound_in_reaction(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(id="v2", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
            )
        )
        m.remove_reaction("v1")
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, set(["v2"]))
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, set(["v2"]))

    def test_remove_reactions_tuple(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(id="v2", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
                Reaction(id="v3", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
            )
        )
        m.remove_reactions(("v1", "v3"))
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, set(["v2"]))
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, set(["v2"]))

    def test_remove_reactions_list(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(id="v2", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
                Reaction(id="v3", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
            )
        )
        m.remove_reactions(["v1", "v3"])
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, set(["v2"]))
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, set(["v2"]))

    def test_remove_reactions_set(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(id="v2", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
                Reaction(id="v3", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
            )
        )
        m.remove_reactions({"v1", "v3"})
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, set(["v2"]))
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, set(["v2"]))

    def test_remove_reactions_dict(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(id="v2", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
                Reaction(id="v3", stoichiometries={"cpd1_c": 1, "cpd2_c": -1}),
            )
        )
        m.remove_reactions({"v1": 1, "v3": 1})
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, set(["v2"]))
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, set(["v2"]))

    def test_get_reversible_reactions(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_reactions(
            (
                Reaction(id="v_irrev", reversible=False),
                Reaction(id="v_rev", reversible=True),
            )
        )
        self.assertEqual(m.get_reversible_reactions(), ["v_rev"])

    def test_get_irreversible_reactions(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_reactions(
            (
                Reaction(id="v_irrev", reversible=False),
                Reaction(id="v_rev", reversible=True),
            )
        )
        self.assertEqual(m.get_irreversible_reactions(), ["v_irrev"])

    def test_add_pathway(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_reactions((Reaction(id="v1"), Reaction(id="v2"), Reaction(id="v3"),))
        m.add_pathway("pwy-101", ["v2", "v3"])
        self.assertEqual(m.pathways, {"pwy-101": {"v2", "v3"}})

    def test_add_pathway_reaction_attribute(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_reactions((Reaction(id="v1"), Reaction(id="v2"), Reaction(id="v3"),))
        m.add_pathway("pwy-101", ["v2", "v3"])
        self.assertEqual(m.reactions["v1"].pathways, set())
        self.assertEqual(m.reactions["v2"].pathways, {"pwy-101"})
        self.assertEqual(m.reactions["v3"].pathways, {"pwy-101"})

    def test_get_reactions_of_pathway(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_reactions((Reaction(id="v1"), Reaction(id="v2"), Reaction(id="v3"),))
        m.add_pathway("pwy-101", ["v2", "v3"])
        self.assertEqual(m.get_reactions_of_pathway("pwy-101"), {"v2", "v3"})

    def test_get_pathway_ids(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_reactions((Reaction(id="v1"), Reaction(id="v2"), Reaction(id="v3"),))
        m.add_pathway("pwy-101", ["v2", "v3"])
        self.assertEqual(m.get_pathway_ids(), ("pwy-101",))

    def test_add_transport_reaction_c_p(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        m.add_transport_reaction(compound_id="cpd1_c", compartment_id="PERIPLASM")
        self.assertEqual(tuple(m.compounds.keys()), ("cpd1_c", "cpd1_p"))
        self.assertEqual(
            m.reactions["TR_cpd1_c_p"].stoichiometries, {"cpd1_c": -1, "cpd1_p": 1}
        )

    def test_add_transport_reaction_p_c(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="PERIPLASM"))
        m.add_transport_reaction(compound_id="cpd1_p", compartment_id="CYTOSOL")
        self.assertEqual(tuple(m.compounds.keys()), ("cpd1_p", "cpd1_c"))
        self.assertEqual(
            m.reactions["TR_cpd1_p_c"].stoichiometries, {"cpd1_p": -1, "cpd1_c": 1}
        )

    def test_add_transport_reaction_c_e(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        m.add_transport_reaction(compound_id="cpd1_c", compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds.keys()), ("cpd1_c", "cpd1_e"))
        self.assertEqual(
            m.reactions["TR_cpd1_c_e"].stoichiometries, {"cpd1_c": -1, "cpd1_e": 1}
        )

    def test_add_transport_reaction_e_c(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="EXTRACELLULAR"))
        m.add_transport_reaction(compound_id="cpd1_e", compartment_id="CYTOSOL")
        self.assertEqual(tuple(m.compounds.keys()), ("cpd1_e", "cpd1_c"))
        self.assertEqual(
            m.reactions["TR_cpd1_e_c"].stoichiometries, {"cpd1_e": -1, "cpd1_c": 1}
        )

    def test_add_transport_reaction_p_e(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="PERIPLASM"))
        m.add_transport_reaction(compound_id="cpd1_p", compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds.keys()), ("cpd1_p", "cpd1_e"))
        self.assertEqual(
            m.reactions["TR_cpd1_p_e"].stoichiometries, {"cpd1_p": -1, "cpd1_e": 1}
        )

    def test_add_transport_reaction_e_p(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="EXTRACELLULAR"))
        m.add_transport_reaction(compound_id="cpd1_e", compartment_id="PERIPLASM")
        self.assertEqual(tuple(m.compounds.keys()), ("cpd1_e", "cpd1_p"))
        self.assertEqual(
            m.reactions["TR_cpd1_e_p"].stoichiometries, {"cpd1_e": -1, "cpd1_p": 1}
        )

    def test_add_influx_cytosol_without_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        m.add_influx("cpd1_c", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_c", "cpd1_e"))
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (-1000, 0))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, False)

    def test_add_influx_cytosol_with_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        m.add_transport_reaction(
            compound_id="cpd1_c", compartment_id="EXTRACELLULAR", bounds=(-1000, 0)
        )
        m.add_influx("cpd1_c", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_c", "cpd1_e"))
        self.assertEqual(
            m.reactions["TR_cpd1_c_e"].stoichiometries, {"cpd1_c": -1, "cpd1_e": 1}
        )
        self.assertEqual(m.reactions["TR_cpd1_c_e"].bounds, (-1000, 0))
        self.assertEqual(m.reactions["TR_cpd1_c_e"].reversible, False)
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (-1000, 0))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, False)

    def test_add_efflux_cytosol_without_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        m.add_efflux("cpd1_c", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_c", "cpd1_e"))
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (0, 1000))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, False)

    def test_add_efflux_cytosol_with_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        m.add_transport_reaction(
            compound_id="cpd1_c", compartment_id="EXTRACELLULAR", bounds=(0, 1000)
        )
        m.add_efflux("cpd1_c", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_c", "cpd1_e"))
        self.assertEqual(
            m.reactions["TR_cpd1_c_e"].stoichiometries, {"cpd1_c": -1, "cpd1_e": 1}
        )
        self.assertEqual(m.reactions["TR_cpd1_c_e"].bounds, (0, 1000))
        self.assertEqual(m.reactions["TR_cpd1_c_e"].reversible, False)
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (0, 1000))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, False)

    def test_add_medium_cytosol_without_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        m.add_medium_component("cpd1_c", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_c", "cpd1_e"))
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (-1000, 1000))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, True)

    def test_add_medium_cytosol_with_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="CYTOSOL"))
        m.add_medium_component("cpd1_c", extracellular_compartment_id="EXTRACELLULAR")
        m.add_transport_reaction(
            compound_id="cpd1_c", compartment_id="EXTRACELLULAR", bounds=(-1000, 1000)
        )
        self.assertEqual(tuple(m.compounds), ("cpd1_c", "cpd1_e"))
        self.assertEqual(
            m.reactions["TR_cpd1_c_e"].stoichiometries, {"cpd1_c": -1, "cpd1_e": 1}
        )
        self.assertEqual(m.reactions["TR_cpd1_c_e"].bounds, (-1000, 1000))
        self.assertEqual(m.reactions["TR_cpd1_c_e"].reversible, True)
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (-1000, 1000))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, True)

    def test_add_influx_extracellular_without_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="EXTRACELLULAR"))
        m.add_influx("cpd1_e", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_e",))
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (-1000, 0))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, False)

    def test_add_influx_extracellular_with_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="EXTRACELLULAR"))
        m.add_influx("cpd1_e", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_e",))
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (-1000, 0))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, False)

    def test_add_efflux_extracellular_without_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="EXTRACELLULAR"))
        m.add_efflux("cpd1_e", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_e",))
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (0, 1000))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, False)

    def test_add_efflux_extracellular_with_transporters(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="EXTRACELLULAR"))
        m.add_efflux("cpd1_e", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_e",))
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (0, 1000))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, False)

    def test_add_medium_extracellular_without_transporter(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="EXTRACELLULAR"))
        m.add_medium_component("cpd1_e", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_e",))
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (-1000, 1000))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, True)

    def test_add_medium_extracellular_with_transporter(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compound(Compound(base_id="cpd1", compartment="EXTRACELLULAR"))
        m.add_medium_component("cpd1_e", extracellular_compartment_id="EXTRACELLULAR")
        self.assertEqual(tuple(m.compounds), ("cpd1_e",))
        self.assertEqual(m.reactions["EX_cpd1_e"].stoichiometries, {"cpd1_e": -1})
        self.assertEqual(m.reactions["EX_cpd1_e"].bounds, (-1000, 1000))
        self.assertEqual(m.reactions["EX_cpd1_e"].reversible, True)

    def test_set_objective(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.set_objective({"v1": 1, "v2": 2})
        self.assertEqual(m.objective, {"v1": 1, "v2": 2})

    def test_get_stoichiometric_matrix(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(id="v2", stoichiometries={"cpd2_c": -1, "cpd3_c": 1}),
            )
        )
        self.assertTrue(
            np.all(
                np.equal(
                    m.get_stoichiometric_matrix(),
                    np.array([[-1.0, 0.0], [1.0, -1.0], [0.0, 1.0]]),
                )
            )
        )

    def test_get_stoichiometric_df(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(id="v2", stoichiometries={"cpd2_c": -1, "cpd3_c": 1}),
            )
        )
        df = m.get_stoichiometric_df()
        self.assertEqual(tuple(df.index), ("cpd1_c", "cpd2_c", "cpd3_c"))
        self.assertEqual(tuple(df.columns), ("v1", "v2"))

    def test_reversibility_duplication(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v_default", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(
                    id="v_irrev",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    reversible=False,
                ),
                Reaction(
                    id="v_rev",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    reversible=True,
                ),
            )
        )
        m.reversibility_duplication()
        self.assertEqual(
            tuple(m.reactions.keys()), ("v_default", "v_irrev", "v_rev", "v_rev__rev__")
        )
        self.assertEqual(
            m.reactions["v_rev"].stoichiometries, {"cpd1_c": -1, "cpd2_c": 1}
        )
        self.assertEqual(
            m.reactions["v_rev__rev__"].stoichiometries, {"cpd1_c": 1, "cpd2_c": -1}
        )

    def test_remove_reversibility_duplication(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(id="v_default", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),
                Reaction(
                    id="v_irrev",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    reversible=False,
                ),
                Reaction(
                    id="v_rev",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    reversible=True,
                ),
            )
        )
        m.reversibility_duplication()
        m.remove_reversibility_duplication()
        self.assertEqual(tuple(m.reactions.keys()), ("v_default", "v_irrev", "v_rev"))
        self.assertEqual(
            m.reactions["v_rev"].stoichiometries, {"cpd1_c": -1, "cpd2_c": 1}
        )

    def test_cofactor_duplication(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="v0",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                ),
                Reaction(
                    id="v1", stoichiometries={"cpd1_c": -1, "ATP_c": -1, "cpd2_c": 1}
                ),
                Reaction(
                    id="v2", stoichiometries={"cpd1_c": -1, "cpd2_c": 1, "ADP_c": 1}
                ),
            )
        )
        m.cofactor_pairs = {"ATP_c": "ADP_c"}
        m.cofactor_duplication()
        self.assertEqual(
            tuple(m.compounds),
            ("cpd1_c", "cpd2_c", "ATP_c", "ADP_c", "ATP_c__cof__", "ADP_c__cof__",),
        )
        self.assertEqual(tuple(m.reactions), ("v0", "v1", "v2", "v0__cof__"))
        self.assertEqual(
            m.reactions["v0"].stoichiometries,
            {"cpd1_c": -1, "cpd2_c": 1, "ATP_c": -1, "ADP_c": 1},
        )
        self.assertEqual(
            m.reactions["v1"].stoichiometries, {"cpd1_c": -1, "ATP_c": -1, "cpd2_c": 1}
        )
        self.assertEqual(
            m.reactions["v2"].stoichiometries, {"cpd1_c": -1, "cpd2_c": 1, "ADP_c": 1}
        )
        self.assertEqual(
            m.reactions["v0__cof__"].stoichiometries,
            {"cpd1_c": -1, "cpd2_c": 1, "ATP_c__cof__": -1, "ADP_c__cof__": 1},
        )

    def test_remove_cofactor_duplication(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="v0",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                ),
                Reaction(
                    id="v1", stoichiometries={"cpd1_c": -1, "ATP_c": -1, "cpd2_c": 1}
                ),
                Reaction(
                    id="v2", stoichiometries={"cpd1_c": -1, "cpd2_c": 1, "ADP_c": 1}
                ),
            )
        )
        m.cofactor_duplication()
        m.remove_cofactor_duplication()
        self.assertEqual(tuple(m.compounds), ("cpd1_c", "cpd2_c", "ATP_c", "ADP_c"))
        self.assertEqual(tuple(m.reactions), ("v0", "v1", "v2"))
        self.assertEqual(
            m.reactions["v0"].stoichiometries,
            {"cpd1_c": -1, "cpd2_c": 1, "ATP_c": -1, "ADP_c": 1},
        )
        self.assertEqual(
            m.reactions["v1"].stoichiometries, {"cpd1_c": -1, "ATP_c": -1, "cpd2_c": 1}
        )
        self.assertEqual(
            m.reactions["v2"].stoichiometries, {"cpd1_c": -1, "cpd2_c": 1, "ADP_c": 1}
        )


class QualityControlTests(unittest.TestCase):
    def test_charge_balance_both_zero(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", charge=0),
                Compound(base_id="cpd2", compartment="CYTOSOL", charge=0),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),)
        )
        self.assertTrue(m.check_charge_balance("v1"))

    def test_charge_balance_both_one(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", charge=1),
                Compound(base_id="cpd2", compartment="CYTOSOL", charge=1),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),)
        )
        self.assertTrue(m.check_charge_balance("v1"))

    def test_charge_balance_substrate_stoichiometry(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", charge=1),
                Compound(base_id="cpd2", compartment="CYTOSOL", charge=2),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -2, "cpd2_c": 1}),)
        )
        self.assertTrue(m.check_charge_balance("v1"))

    def test_charge_balance_product_stoichiometry(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", charge=2),
                Compound(base_id="cpd2", compartment="CYTOSOL", charge=1),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 2}),)
        )
        self.assertTrue(m.check_charge_balance("v1"))

    def test_charge_balance_fail_on_opposite_signs(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", charge=-1),
                Compound(base_id="cpd2", compartment="CYTOSOL", charge=1),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),)
        )
        self.assertFalse(m.check_charge_balance("v1"))

    def test_charge_balance_fail_on_opposite_signs2(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", charge=1),
                Compound(base_id="cpd2", compartment="CYTOSOL", charge=-1),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),)
        )
        self.assertFalse(m.check_charge_balance("v1"))

    def test_mass_balance_single_atom(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", formula={"C": 1}),
                Compound(base_id="cpd2", compartment="CYTOSOL", formula={"C": 1}),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),)
        )
        self.assertTrue(m.check_mass_balance("v1"))

    def test_mass_balance_multiple_atoms(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(
                    base_id="cpd1",
                    compartment="CYTOSOL",
                    formula={"C": 6, "H": 12, "O": 6},
                ),
                Compound(
                    base_id="cpd2",
                    compartment="CYTOSOL",
                    formula={"C": 6, "H": 12, "O": 6},
                ),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 1}),)
        )
        self.assertTrue(m.check_mass_balance("v1"))

    def test_mass_balance_multiple_compounds(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(
                    base_id="cpd1",
                    compartment="CYTOSOL",
                    formula={"C": 6, "H": 12, "O": 6},
                ),
                Compound(
                    base_id="cpd2",
                    compartment="CYTOSOL",
                    formula={"C": 6, "H": 12, "O": 6},
                ),
                Compound(base_id="cpd3", compartment="CYTOSOL", formula={"C": 6}),
                Compound(base_id="cpd4", compartment="CYTOSOL", formula={"C": 6}),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="v1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "cpd3_c": -2,
                        "cpd2_c": 1,
                        "cpd4_c": 2,
                    },
                ),
            )
        )
        self.assertTrue(m.check_mass_balance("v1"))

    def test_mass_balance_multiple_atoms_substrate_stoichiometry(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(
                    base_id="cpd1",
                    compartment="CYTOSOL",
                    formula={"C": 3, "H": 6, "O": 3},
                ),
                Compound(
                    base_id="cpd2",
                    compartment="CYTOSOL",
                    formula={"C": 6, "H": 12, "O": 6},
                ),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -2, "cpd2_c": 1}),)
        )
        self.assertTrue(m.check_mass_balance("v1"))

    def test_mass_balance_multiple_atoms_product_stoichiometry(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(
                    base_id="cpd1",
                    compartment="CYTOSOL",
                    formula={"C": 6, "H": 12, "O": 6},
                ),
                Compound(
                    base_id="cpd2",
                    compartment="CYTOSOL",
                    formula={"C": 3, "H": 6, "O": 3},
                ),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 2}),)
        )
        self.assertTrue(m.check_mass_balance("v1"))

    def test_mass_balance_fail_on_missing_substrate_formula(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", formula={}),
                Compound(
                    base_id="cpd2",
                    compartment="CYTOSOL",
                    formula={"C": 3, "H": 6, "O": 3},
                ),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 2}),)
        )
        self.assertFalse(m.check_mass_balance("v1"))

    def test_mass_balance_fail_on_missing_product_formula(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(
                    base_id="cpd1",
                    compartment="CYTOSOL",
                    formula={"C": 3, "H": 6, "O": 3},
                ),
                Compound(base_id="cpd2", compartment="CYTOSOL", formula={}),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 2}),)
        )
        self.assertFalse(m.check_mass_balance("v1"))

    def test_mass_balance_fail_on_missing_substrate_atom(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", formula={"C": 1}),
                Compound(
                    base_id="cpd2", compartment="CYTOSOL", formula={"C": 1, "H": 1}
                ),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 2}),)
        )
        self.assertFalse(m.check_mass_balance("v1"))

    def test_mass_balance_fail_on_missing_product_atom(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m.add_compounds(
            (
                Compound(
                    base_id="cpd1", compartment="CYTOSOL", formula={"C": 1, "H": 1}
                ),
                Compound(base_id="cpd2", compartment="CYTOSOL", formula={"C": 1}),
            )
        )
        m.add_reactions(
            (Reaction(id="v1", stoichiometries={"cpd1_c": -1, "cpd2_c": 2}),)
        )
        self.assertFalse(m.check_mass_balance("v1"))


class UpdateFromReferenceTests(unittest.TestCase):
    def test_add_cpd_from_ref_new(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compound(
            Compound(
                base_id="cpd1",
                compartment="CYTOSOL",
                formula={"C": 1},
                charge=1,
                gibbs0=10,
                smiles="abc",
                types=["cpd"],
            )
        )
        m.add_compound_from_reference(db, "cpd1_c")
        cpd = m.compounds["cpd1_c"]
        self.assertEqual(cpd.id, "cpd1_c")
        self.assertEqual(cpd.formula, {"C": 1})
        self.assertEqual(cpd.charge, 1)
        self.assertEqual(cpd.gibbs0, 10)
        self.assertEqual(cpd.smiles, "abc")
        self.assertEqual(cpd.types, ["cpd"])
        self.assertEqual(cpd.in_reaction, set())

    def test_add_cpd_from_ref_existing(self):
        """Should keep the in_reaction attribute"""
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)

        db.add_compounds(
            (
                Compound(
                    base_id="cpd1",
                    compartment="CYTOSOL",
                    formula={"C": 1},
                    charge=1,
                    gibbs0=10,
                    smiles="abc",
                    types=["cpd"],
                    in_reaction={"rxn2_c"},
                ),
            )
        )
        m.add_compounds(
            (Compound(base_id="cpd1", compartment="CYTOSOL", in_reaction={"rxn1_c"}),)
        )
        m.add_compound_from_reference(db, "cpd1_c")
        cpd = m.compounds["cpd1_c"]
        self.assertEqual(cpd.id, "cpd1_c")
        self.assertEqual(cpd.formula, {"C": 1})
        self.assertEqual(cpd.charge, 1)
        self.assertEqual(cpd.gibbs0, 10)
        self.assertEqual(cpd.smiles, "abc")
        self.assertEqual(cpd.types, ["cpd"])
        self.assertEqual(cpd.in_reaction, {"rxn1_c"})

    def test_add_reaction_from_ref_new(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                ),
                Reaction(
                    id="rxn2_c",
                    base_id="rxn2",
                    stoichiometries={"cpd2_c": -1, "cpd3_c": 1},
                ),
                Reaction(
                    id="rxn3_c",
                    base_id="rxn3",
                    stoichiometries={"cpd1_c": -1, "cpd3_c": 1},
                    pathways={"pwy1"},
                ),
            ),
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                ),
                Reaction(
                    id="rxn2_c",
                    base_id="rxn2",
                    stoichiometries={"cpd2_c": -1, "cpd3_c": 1},
                ),
            )
        )
        m.add_reaction_from_reference(db, "rxn3_c")
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, {"rxn1_c", "rxn3_c"})
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, {"rxn1_c", "rxn2_c"})
        self.assertEqual(m.compounds["cpd3_c"].in_reaction, {"rxn2_c", "rxn3_c"})
        self.assertEqual(dict(m.pathways), {"pwy1": {"rxn3_c"}})

    def test_add_reaction_replacing(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            ),
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                ),
                Reaction(
                    id="rxn2_c",
                    base_id="rxn2",
                    stoichiometries={"cpd2_c": -1, "cpd3_c": 1},
                ),
                Reaction(
                    id="rxn3_c",
                    base_id="rxn3",
                    stoichiometries={"cpd1_c": -1, "cpd3_c": 1},
                    reversible=True,
                    pathways={"pwy0"},
                ),
            ),
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="cpd3", compartment="CYTOSOL"),
            ),
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                ),
                Reaction(
                    id="rxn2_c",
                    base_id="rxn2",
                    stoichiometries={"cpd2_c": -1, "cpd3_c": 1},
                ),
                Reaction(
                    id="rxn3_c",
                    base_id="rxn3",
                    stoichiometries={"cpd2_c": -2, "cpd3_c": 2},
                    reversible=False,
                    pathways={"pwy1"},
                ),
            )
        )
        m.add_reaction_from_reference(db, "rxn3_c")
        self.assertEqual(m.compounds["cpd1_c"].in_reaction, {"rxn1_c", "rxn3_c"})
        self.assertEqual(m.compounds["cpd2_c"].in_reaction, {"rxn1_c", "rxn2_c"})
        self.assertEqual(m.compounds["cpd3_c"].in_reaction, {"rxn2_c", "rxn3_c"})

        self.assertEqual(
            m.reactions["rxn3_c"].stoichiometries, {"cpd1_c": -1, "cpd3_c": 1}
        )
        self.assertTrue(m.reactions["rxn3_c"].reversible)
        self.assertEqual(dict(m.pathways), {"pwy0": {"rxn3_c"}})

    def test_add_from_reference(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                ),
            )
        )
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1_c")
        self.assertEqual(set(m.compounds.keys()), {"cpd1_c", "cpd2_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c"})

    def test_add_from_reference_cof_removal_afterwards(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"ATP_c": -1, "ADP_c": 1},
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1_c")
        self.assertEqual(
            set(m.compounds.keys()), {"ATP_c", "ATP_c__cof__", "ADP_c__cof__", "ADP_c"}
        )
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c", "rxn1_c__cof__"})
        m.remove_cofactor_duplication()
        self.assertEqual(set(m.compounds.keys()), {"ATP_c", "ADP_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c"})

    def test_add_from_reference_cof_removal_afterwards_2(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"ATP_c": -1, "ADP_c": 1},
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1_c__cof__")
        self.assertEqual(
            set(m.compounds.keys()), {"ATP_c", "ATP_c__cof__", "ADP_c__cof__", "ADP_c"}
        )
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c", "rxn1_c__cof__"})
        m.remove_cofactor_duplication()
        self.assertEqual(set(m.compounds.keys()), {"ATP_c", "ADP_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c"})

    def test_add_from_reference_rev_removal_afterwards(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    reversible=True,
                ),
            )
        )
        db.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1_c")
        self.assertEqual(set(m.compounds.keys()), {"cpd1_c", "cpd2_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c", "rxn1_c__rev__"})
        m.remove_reversibility_duplication()
        self.assertEqual(set(m.compounds.keys()), {"cpd1_c", "cpd2_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c"})

    def test_add_from_reference_rev_removal_afterwards_2(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    reversible=True,
                ),
            )
        )
        db.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1_c__rev__")
        self.assertEqual(set(m.compounds.keys()), {"cpd1_c", "cpd2_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c", "rxn1_c__rev__"})
        m.remove_reversibility_duplication()
        self.assertEqual(set(m.compounds.keys()), {"cpd1_c", "cpd2_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c"})

    def test_add_from_reference_cof(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1_c")
        self.assertEqual(
            set(m.compounds.keys()),
            {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c", "ATP_c__cof__", "ADP_c__cof__",},
        )
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c", "rxn1_c__cof__"})

    def test_add_from_reference_rev(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    reversible=True,
                ),
            )
        )
        db.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1_c")
        self.assertEqual(set(m.compounds.keys()), {"cpd1_c", "cpd2_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c", "rxn1_c__rev__"})

    def test_add_from_reference_cof_and_rev(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1_c")
        self.assertEqual(
            set(m.compounds.keys()),
            {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c", "ATP_c__cof__", "ADP_c__cof__",},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {"rxn1_c", "rxn1_c__rev__", "rxn1_c__cof____rev__", "rxn1_c__cof__"},
        )

    def test_add_from_reference_var_base_id(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1")
        self.assertEqual(
            set(m.compounds.keys()), {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c"},
        )
        self.assertEqual(
            set(m.reactions.keys()), {"rxn1__var__0_c", "rxn1__var__1_c"},
        )

    def test_add_from_reference_var_id(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1__var__0_c")
        self.assertEqual(
            set(m.compounds.keys()), {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c"},
        )
        self.assertEqual(
            set(m.reactions.keys()), {"rxn1__var__0_c", "rxn1__var__1_c"},
        )

    def test_add_from_reference_var_cof_rev_base_id(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1")
        self.assertEqual(
            set(m.compounds.keys()),
            {"ATP_c__cof__", "ADP_c__cof__", "ADP_c", "cpd2_c", "ATP_c", "cpd1_c"},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {
                "rxn1__var__0_c",
                "rxn1__var__0_c__cof__",
                "rxn1__var__0_c__rev__",
                "rxn1__var__0_c__cof____rev__",
                "rxn1__var__1_c",
                "rxn1__var__1_c__cof__",
                "rxn1__var__1_c__rev__",
                "rxn1__var__1_c__cof____rev__",
            },
        )

    def test_add_from_reference_var_cof_rev_id(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1__var__0_c")
        self.assertEqual(
            set(m.compounds.keys()),
            {"ATP_c__cof__", "ADP_c__cof__", "ADP_c", "cpd2_c", "ATP_c", "cpd1_c"},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {
                "rxn1__var__0_c",
                "rxn1__var__0_c__cof__",
                "rxn1__var__0_c__rev__",
                "rxn1__var__0_c__cof____rev__",
                "rxn1__var__1_c",
                "rxn1__var__1_c__cof__",
                "rxn1__var__1_c__rev__",
                "rxn1__var__1_c__cof____rev__",
            },
        )

    def test_replace_from_reference(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_old_c": -1, "cpd2_old_c": 1},
                ),
            )
        )
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1_c")
        self.assertEqual(set(m.compounds.keys()), {"cpd1_c", "cpd2_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c"})

    def test_replace_from_reference_cof(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_old_c": -1,
                        "ATP_c": -1,
                        "cpd2_old_c": 1,
                        "ADP_c": 1,
                    },
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        m.cofactor_pairs = {"ATP_c": "ADP_c"}
        m.cofactor_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1")
        self.assertEqual(
            set(m.compounds.keys()),
            {"cpd1_c", "cpd2_c", "ATP_c", "ADP_c", "ATP_c__cof__", "ADP_c__cof__",},
        )
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c", "rxn1_c__cof__"})

    def test_replace_from_reference_rev(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                    reversible=True,
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_old_c": -1, "cpd2_old_c": 1},
                    reversible=True,
                ),
            )
        )
        db.reversibility_duplication()
        m.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1")
        self.assertEqual(set(m.compounds.keys()), {"cpd1_c", "cpd2_c"})
        self.assertEqual(set(m.reactions.keys()), {"rxn1_c", "rxn1_c__rev__"})

    def test_replace_from_reference_cof_and_rev(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_old_c": -1,
                        "ATP_c": -1,
                        "cpd2_old_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1")
        self.assertEqual(
            set(m.compounds.keys()),
            {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c", "ATP_c__cof__", "ADP_c__cof__",},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {"rxn1_c", "rxn1_c__rev__", "rxn1_c__cof____rev__", "rxn1_c__cof__"},
        )

    def test_replace_from_reference_var_base_id(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_old_c": -1,
                        "ATP_c": -1,
                        "cpd2_old_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_old_c": -1,
                        "ATP_c": -1,
                        "cpd2_old_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1")
        self.assertEqual(
            set(m.compounds.keys()), {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c"},
        )
        self.assertEqual(
            set(m.reactions.keys()), {"rxn1__var__0_c", "rxn1__var__1_c"},
        )

    def test_replace_from_reference_var_id(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_old_c": -1,
                        "ATP_c": -1,
                        "cpd2_old_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1__var__0_c")
        self.assertEqual(
            set(m.compounds.keys()), {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c"},
        )
        self.assertEqual(
            set(m.reactions.keys()), {"rxn1__var__0_c", "rxn1__var__1_c"},
        )

    def test_replace_from_reference_var_cof_rev_base_id(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_old_c": -1,
                        "ATP_c": -1,
                        "cpd2_old_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.cofactor_pairs = {"ATP_c": "ADP_c"}
        m.cofactor_duplication()
        m.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1")
        self.assertEqual(
            set(m.compounds.keys()),
            {"ATP_c__cof__", "ADP_c__cof__", "ADP_c", "cpd2_c", "ATP_c", "cpd1_c"},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {
                "rxn1__var__0_c",
                "rxn1__var__0_c__cof__",
                "rxn1__var__0_c__rev__",
                "rxn1__var__0_c__cof____rev__",
                "rxn1__var__1_c",
                "rxn1__var__1_c__cof__",
                "rxn1__var__1_c__rev__",
                "rxn1__var__1_c__cof____rev__",
            },
        )

    def test_replace_from_reference_var_cof_rev_id(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
                Reaction(
                    id="rxn1__var__1_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_old_c": -1,
                        "ATP_c": -1,
                        "cpd2_old_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.cofactor_pairs = {"ATP_c": "ADP_c"}
        m.cofactor_duplication()
        m.reversibility_duplication()
        m.add_reaction_from_reference(reference_model=db, reaction_id="rxn1__var__0_c")
        self.assertEqual(
            set(m.compounds.keys()),
            {"ATP_c__cof__", "ADP_c__cof__", "ADP_c", "cpd2_c", "ATP_c", "cpd1_c"},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {
                "rxn1__var__0_c",
                "rxn1__var__0_c__rev__",
                "rxn1__var__0_c__cof__",
                "rxn1__var__0_c__cof____rev__",
                "rxn1__var__1_c",
                "rxn1__var__1_c__rev__",
                "rxn1__var__1_c__cof__",
                "rxn1__var__1_c__cof____rev__",
            },
        )

    def test_add_from_reference_rev_input(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.add_reaction_from_reference(
            reference_model=db, reaction_id="rxn1__var__0_c__rev__"
        )
        self.assertEqual(
            set(m.compounds.keys()),
            {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c", "ATP_c__cof__", "ADP_c__cof__",},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {
                "rxn1__var__0_c",
                "rxn1__var__0_c__rev__",
                "rxn1__var__0_c__cof__",
                "rxn1__var__0_c__cof____rev__",
            },
        )

    def test_add_from_reference_cof_input(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.add_reaction_from_reference(
            reference_model=db, reaction_id="rxn1__var__0_c__cof__"
        )
        self.assertEqual(
            set(m.compounds.keys()),
            {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c", "ATP_c__cof__", "ADP_c__cof__",},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {
                "rxn1__var__0_c",
                "rxn1__var__0_c__rev__",
                "rxn1__var__0_c__cof__",
                "rxn1__var__0_c__cof____rev__",
            },
        )

    def test_replace_from_reference_rev_input(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_old_c": -1,
                        "ATP_c": -1,
                        "cpd2_old_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.cofactor_pairs = {"ATP_c": "ADP_c"}
        m.cofactor_duplication()
        m.reversibility_duplication()
        m.add_reaction_from_reference(
            reference_model=db, reaction_id="rxn1__var__0_c__rev__"
        )
        self.assertEqual(
            set(m.compounds.keys()),
            {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c", "ATP_c__cof__", "ADP_c__cof__",},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {
                "rxn1__var__0_c",
                "rxn1__var__0_c__rev__",
                "rxn1__var__0_c__cof__",
                "rxn1__var__0_c__cof____rev__",
            },
        )

    def test_replace_from_reference_cof_input(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL"),
                Compound(base_id="cpd2", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_c": -1,
                        "ATP_c": -1,
                        "cpd2_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1_old", compartment="CYTOSOL"),
                Compound(base_id="cpd2_old", compartment="CYTOSOL"),
                Compound(base_id="ATP", compartment="CYTOSOL"),
                Compound(base_id="ADP", compartment="CYTOSOL"),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn1__var__0_c",
                    base_id="rxn1",
                    stoichiometries={
                        "cpd1_old_c": -1,
                        "ATP_c": -1,
                        "cpd2_old_c": 1,
                        "ADP_c": 1,
                    },
                    reversible=True,
                ),
            )
        )
        db.cofactor_pairs = {"ATP_c": "ADP_c"}
        db.cofactor_duplication()
        db.reversibility_duplication()
        m.cofactor_pairs = {"ATP_c": "ADP_c"}
        m.cofactor_duplication()
        m.reversibility_duplication()
        m.add_reaction_from_reference(
            reference_model=db, reaction_id="rxn1__var__0_c__cof__"
        )
        self.assertEqual(
            set(m.compounds.keys()),
            {"cpd1_c", "ATP_c", "cpd2_c", "ADP_c", "ATP_c__cof__", "ADP_c__cof__",},
        )
        self.assertEqual(
            set(m.reactions.keys()),
            {
                "rxn1__var__0_c",
                "rxn1__var__0_c__rev__",
                "rxn1__var__0_c__cof__",
                "rxn1__var__0_c__cof____rev__",
            },
        )

    def test_update_model_remove_unbalanced(self):
        compounds = {}
        reactions = {}
        compartments = {"CYTOSOL": "c", "PERIPLASM": "p", "EXTRACELLULAR": "e"}
        db = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        m = Model(compounds=compounds, reactions=reactions, compartments=compartments)
        db.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", charge=1),
                Compound(base_id="cpd2", compartment="CYTOSOL", charge=1),
            )
        )
        db.add_reactions(
            (
                Reaction(
                    id="rxn1_c",
                    base_id="rxn1",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 1},
                ),
            )
        )
        m.add_compounds(
            (
                Compound(base_id="cpd1", compartment="CYTOSOL", charge=2),
                Compound(base_id="cpd2", compartment="CYTOSOL", charge=1),
            )
        )
        m.add_reactions(
            (
                Reaction(
                    id="rxn2",
                    base_id="rxn2",
                    stoichiometries={"cpd1_c": -1, "cpd2_c": 2},
                ),
            )
        )
        m.update_from_reference(db)
        self.assertEqual(m.reactions, {})
