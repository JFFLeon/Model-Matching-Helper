# Model-Matching-Helper
by jff_leon444_  , better Model-Matching-Helper

This Python code can read your .vmr from which airplanes are there and replaces them with any airplanes you can define in your .txt.
The output then comes out formatted in a new vmr file.

Example:
input.vmr : 
<?xml version="1.0" encoding="utf-8"?>
<ModelMatchRuleSet>
     <ModelMatchRule TypeCode="C172 "ModelName="VATSIM_GA_C172" />
</ModelMatchRuleSet>

Extended_Modelmatching.txt :
C172   C170			
C172   C175			
C172   C177			
C172   C180

externaloutput.vmr :
<?xml version="1.0" encoding="utf-8"?>
<ModelMatchRuleSet>
    <ModelMatchRule TypeCode="C170" ModelName="VATSIM_GA_C172" />
	<ModelMatchRule TypeCode="C175" ModelName="VATSIM_GA_C172" />
	<ModelMatchRule TypeCode="C177" ModelName="VATSIM_GA_C172" />
	<ModelMatchRule TypeCode="C180" ModelName="VATSIM_GA_C172" />
</ModelMatchRuleSet>

DISCORD: jff_leon444_
