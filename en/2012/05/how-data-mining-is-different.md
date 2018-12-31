# How Data Mining is Different

Much of the important scientific and technological development of the last four hundred years comes from a style of investigation, probably best described by Karl Popper, based on controlled experiments. Researchers construct hypotheses inductively, but usually guided by anomalies in existig explanations of ‘how things work’. Such hypotheses should have more explanatory power than existing theories, and should be easier to falsify. Suppose a new hypothesis predicts that cause A is responsible for effect B. A controlled experiment sets up two situations, one in which cause A is present and the other in which it is not. The two situations are, as far as possible, matched with respect to all of the other variables that might influence the presence or absence of effect B. The experiment then looks at whether effect B is present only in the first situation.

Of course, few dependencies of effect on cause are perfect, so we might expect that effect B is not present in some situations where cause A is present, and vice versa. A great deal of statistical machinery has been developed to help determine how much discrepancy can exist and still be appropriate to conclude that there is a dependency of effect B on cause A. If an experiment fails to falsify a hypothesis then this adds credibility to the hypothesis, which may eventually be promoted to a theory. Theories are not considered to be ground truth, but only approximations with useful predictiveness. This approach to understanding the universe has been enormously successful.

However, it is limited by the fact that there are four kinds of settings where controlled experiments are not directly possible: 

1) We do not have access to the variables that we would like to control. Controlled experiments are only possible on earth or its near vicinity. Understanding the wider universe cannot, at present, be achieved by controlled experiments because we cannot control the position, interactions and outputs of stars, galaxies, and other celestial objects. We can observe such objects, but we have no way to set them up in an experimental configuration.
  
2) We do not know how to set the values of variables that we wish to control. Some processes are not well enough understood for us to create experimental configurations on demand. For example, fluid flowing next to a boundary will occasionally throw off turbulent eddies. However, it is not known how to make this happen. Studying the structure of such eddies requires waiting for them to happen, rather than making them happen.

3) It would be unethical to set some variables to some values. Controlled medical experiments on human subjects can only take place if the expected differences between the control and treatment groups are small. If the treatment turns out to be either surprisingly effective or dangerously ineffective, the experiment must be halted on ethical grounds.
  
 4) The values of some variables come from the autonomous actions of humans. Controlled experiments in social, political, and economic settings cannot be constructed because the participants act in their own interests, regardless of the desires of the experimenters. Governments and bureaucrats have tried to avoid these limitations by trying to compel the ‘right’ behavior by participants, but this has been notably unsuccessful.

Controlled experiments require very precise collection of data, capturing the presence or absence of a supposed cause and the corresponding effect, with all other variable values or attributes either held constant, or matched between the two possibilities. In situations where controlled experiments are not possible, such different configurations cannot be created to order, but they may nevertheless be present in data collected about the system of interest. For  example, even though we cannot make stars behave in certain ways, we may be able to find two situations where the presence and absence of a hypothesized cause can be distinguished. The data from such situations can be analyzed to see whether the expected relationship between cause and effect is supported. These are called natural experiments, in contrast to controlled experiments.

In natural experiments, it may often be more difficult to make sure that the values of other variables or attributes are properly matched, but this can be compensated for, to some extent, by the availability of a larger amount of data than could be collected in a controlled experiment. More sophisticated methods for arguing that dependencies imply causality are also needed.

Data mining provides techniques for this second kind of analysis, of systems too complex or inaccessible for controlled experiments. 















