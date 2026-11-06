## Games
- Tic-Tac-Toe
- Connect Four
- Battleship

## Fomrat:
- Section 1 (1h30m): A coding exercise where you'll be tasked with completing the logic for a game. It'll be stubbed out for you to start. You will choose from one of these languages: C#, Java, JavaScript, Python. We will provide a laptop with a couple IDE options, language support, some common keybinding extensions already downloaded, and some searchable dev docs. Success will be gauged by total functionality completed. The whole thing is CLI based, so no GUI. AI agent/chat use is not allowed for this challenge.
- Section 2 (30m): A white-boarding problem with a Redo engineer. Study up on graph problems, memoization, binary tree traversals and more.
- Section 3 (30m): System design for an AI product.
- Section 4 (30m): An experience and architecture discussion with our CTO.




- Leetcode 2328, 329
- Othello
- Leetcode 105, 106 and 889
- Leetcode - 4034 - 3001




A 30-minute system design for an AI product is a product-and-architecture discussion, not a coding problem. They will name a feature that depends on a model and ask you to walk through how you would build it.

At Redo, that feature is likely something in post-purchase commerce: a support agent that answers return questions, a classifier that reads a return reason and suggests approve, deny, or exchange, or search over a merchant's policy documents. The prompt is usually one sentence, such as "Design an assistant that helps a shopper start a return."

They want the shape of the system, not a model-training lecture. In half an hour, cover these pieces:

- Who it is for and what "done" means. A shopper asking about a return, a merchant agent, or an internal tool. Decide what the system is allowed to do on its own and what a human must confirm.
- The request path. The user message comes in, you load the order, the merchant's policy, and recent tickets, then call the model with that context. If the model needs to act, it calls a tool such as "look up order" or "create return." The result goes back to the user and is stored.
- What stays in normal code. Eligibility windows, refund amounts, authentication, and idempotency should not be left to the model. The model can choose an action. Your service checks that the action is allowed.
- How you know it works. You need a set of real tickets with expected answers, a way to grade new prompts against that set, logging of inputs and outputs, and a fallback when the model is unsure or the tool call fails.
- Cost and latency. One call is usually enough for a chat reply. Retrieval plus a tool call is the usual shape. Say what you would cache and what you would not let block the user.

They are not asking you to design Twitter, pick a vector database brand, or derive a training loop. Pick a simple flow, say where the model sits in it, and spend the remaining time on bad answers, unauthorized refunds, and how a human reviews the risky cases.
