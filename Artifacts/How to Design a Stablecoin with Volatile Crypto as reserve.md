\documentclass[12pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath, amssymb, amsfonts, bm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{setspace}
\usepackage{titlesec}
\usepackage{caption}
\usepackage{float} %

\onehalfspacing
\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  citecolor=blue,
  urlcolor=blue
}

\title{\textbf{Designing a Stablecoin with a Highly Volatile Crypto Reserve}}
\author{Hash N  \\
\small Independent Research}
\date{}

\begin{document}
\maketitle

\begin{abstract}
Designing a stablecoin whose collateral is a volatile cryptocurrency such as Ether (ETH) or Bitcoin (BTC) is one of the most difficult challenges in decentralized finance.
The problem is structural: if the collateral’s price $P_t$ can fluctuate by $\pm40\%$ in a day, how can the issued token maintain a stable reference value close to \$ 1?
A robust design must not suppress volatility through discretionary control, but \emph{must contain it mathematically} within a bounded component of the system.
The dual-tranche framework of \textbf{Cao et al. (2023, \textit{Designing Stablecoins})} achieves this by embedding financial-engineering principles---tranching, barrier resets, and option-style payoffs---directly into smart-contract logic.
\end{abstract}

\begin{figure}[H]
    \centering
    \includegraphics[width=1\linewidth]{ETH-USD.png}
    \caption{Historical price of ETH/USD (2017–2025). The chart illustrates the significant volatility of the underlying reserve asset that the stablecoin system is designed to absorb.}
    \label{fig:placeholder}
\end{figure}

\section{Defining Stability as a State Invariant}

Let $P_t$ denote the market price of the reserve asset (e.g., ETH/USD).  
A stablecoin promises that its token $S_t$ maintains a value near \$1 regardless of fluctuations in $P_t$.  
Formally, the system must enforce the solvency constraint:
\begin{equation}
\text{Collateral Value} \ge \text{Stablecoin Liability},
\quad \Rightarrow \quad C_t P_t \ge D_t,
\end{equation}
where $C_t$ is collateral (ETH) and $D_t$ is the dollar-denominated debt represented by outstanding stablecoins.  
The architecture must ensure this inequality holds at all times and that redemptions clear deterministically.  
Stability is therefore not an administrative promise but an \textbf{on-chain invariant}.

\section{The Dual-Class Architecture}

The system’s base layer is a \textbf{Custodian Contract} that securely manages all deposited collateral.  
When a user deposits two units of ETH at price $P_t$, the contract programmatically mints one \textbf{Class A} and one \textbf{Class B} token---two synthetic claims on the same collateral pool.

\begin{table}[h!]
\centering
\begin{tabular}{@{}llll@{}}
\toprule
\textbf{Tranche} & \textbf{Symbol} & \textbf{Behavior} & \textbf{Role} \\ \midrule
Senior (Class A) & $A_t$ & Low volatility; receives periodic coupon $R$ & Stable tranche \\
Junior (Class B) & $B_t$ & Leveraged exposure to ETH & Speculative tranche \\ \bottomrule
\end{tabular}
\caption{Dual-class tranche structure as proposed by Cao et al. (2023).}
\end{table}
\begin{figure}[H]
    \centering
    \includegraphics[width=1\linewidth]{Dual-Tranche Stablecoin Architecture (1).png}
    \caption{System architecture of the dual-tranche stablecoin.}
    \label{fig:placeholder}
\end{figure}
\subsection*{State Variables and NAV Dynamics}

The Custodian maintains the following state variables:

\begin{itemize}
  \item $V_A(t)$: Net Asset Value (NAV) of Class A (senior)
  \item $V_B(t)$: NAV of Class B (junior)
  \item $\beta_t$: Conversion factor maintaining accounting balance
  \item $P_0$: Collateral price at last reset
  \item $H_u, H_d$: Upper and lower NAV barriers
  \item $v_t$: Elapsed time since last reset
  \item $T$: Coupon period (e.g., 100 days)
\end{itemize}

\noindent The system enforces the accounting identity:
\begin{equation}
\beta_t \big(V_A + V_B\big) = \frac{2P_t}{P_0},
\end{equation}
ensuring that two ETH back one pair of $A_t$ and $B_t$.  
The conversion factor $\beta_t$ is updated after each payout or reset to preserve equilibrium.

\paragraph{Leverage Sensitivity}
The instantaneous leverage factor of the junior tranche, $\lambda_t$, is defined as the elasticity of its NAV with respect to the collateral price:
\begin{align}
\lambda_t &= \frac{dV_B/V_B}{dP_t/P_t} = \frac{P_t}{V_B}\frac{dV_B}{dP_t}
= \frac{V_A + V_B}{V_B} = 1 + \frac{V_A}{V_B} > 1.
\end{align}
As $V_B$ decreases during price declines, $\lambda_t$ rises rapidly, motivating a lower barrier $H_d$ to prevent uncontrolled leverage escalation.

\paragraph{Deterministic NAV Evolution}
Between resets, NAVs evolve deterministically:
\begin{align}
V_A(t) &= 1 + R \, v_t,\\
V_B(t) &= \frac{2P_t}{P_0\beta_t} - V_A(t),
\end{align}
where $R$ is the continuous coupon rate paid to Class A holders.  
$V_A$ moves slowly and accrues deterministic yield; $V_B$ amplifies price fluctuations via $\lambda_t>1$.  
This structure mathematically partitions volatility: $V_A$ acts as the safe leg, while $V_B$ internalizes market shocks.

\section{Autonomous Stability Mechanisms}

The hallmark of the design is its self-regulating reset system, which operates without human input.  
The contract continuously evaluates three conditions:

\begin{table}[h!]
\centering
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Condition} & \textbf{Trigger} & \textbf{Outcome} \\ \midrule
$v_t = T$ & Regular payout (time-based) & Pay $R \times T$ ETH to A-holders; update $\beta_t$.\\
$V_B \ge H_u$ & Upward reset (price-based) & Distribute gains; rebase NAVs to 1.\\
$V_B \le H_d$ & Downward reset (price-based) & Realize losses; protect A-holders; merge supply.\\ \bottomrule
\end{tabular}
\caption{Autonomous reset conditions in the Cao et al. model.}
\end{table}

If $V_B < 0$, the contract enters \textbf{Full Liquidation}, paying remaining ETH to A-holders and halting issuance.

\paragraph{Execution Logic}

\textbf{(1) Regular payout}
\begin{equation}
v_t=T:
\begin{cases}
\text{payout}_A = R \times T,\\
\beta_t \leftarrow \text{update},\\
v_t \leftarrow 0
\end{cases}
\end{equation}
This creates predictable fixed-income behavior, like a bond coupon.

\textbf{(2) Upward reset}
\begin{equation}
V_B \ge H_u:
\begin{cases}
A \gets (V_A-1),\\
B \gets (V_B-1),\\
V_A,V_B \leftarrow 1,\\
P_0 \leftarrow P_t,\\
v_t \leftarrow 0
\end{cases}
\end{equation}
Profits are distributed, and the system re-centers leverage.

\textbf{(3) Downward reset}
\begin{equation}
V_B \le H_d:
\begin{cases}
A \gets (V_A-H_d),\\
V_A,V_B \leftarrow 1
\end{cases}
\end{equation}
Class B is effectively recapitalized by supply reduction and the system resets $V_A,V_B$ to 1. This prevents cascading defaults and shields A-holders from black-swan shocks.

\textbf{(4) Full liquidation}
\begin{equation}
V_B < 0:\quad
\text{Pay remaining ETH to A-holders; burn A and B tokens.}
\end{equation}
\begin{figure}[H]
    \centering
    \includegraphics[width=1\linewidth]{Reset Sequence Diagram (1).png}
    \caption{Sequence of function calls and state updates during an upward (or downward) reset.}
    \label{fig:placeholder}
\end{figure}
Each transition is a pure state function of on-chain data, eliminating discretionary control and ensuring equal treatment for all holders.

\section{Second-Layer Split: From Class A to a True Stablecoin}

While Class A is stable relative to ETH volatility, it still appreciates with accrued coupons.  
To derive a transaction-grade stablecoin, the \textbf{Tranche Splitter Contract} decomposes $A_t$ into two sub-claims:
\begin{equation}
A_t \longrightarrow A'_t + B'_t,
\end{equation}
where $A'_t$ is the stablecoin (senior sub-tranche) and $B'_t$ is a leveraged bond (residual sub-tranche).

Mechanically:
\begin{enumerate}
  \item $A_t$ is burned upon deposit.
  \item $A'_t$ and $B'_t$ are minted in equal nominal units.
  \item Redeeming $(A',B') \rightarrow A$ reverses the split.
\end{enumerate}

Let $r_A(t)$ denote Class A’s instantaneous return rate.  
The Splitter directs nearly all of $r_A(t)$ to $B′$, leaving $A′$ approximately constant:
\begin{align}
V_{A'}(t) &\approx 1,\\
V_{B'}(t) &= V_A(t) - 1 + \int_0^t r_A(s)\,ds.
\end{align}
Every dollar of stability in $A'$ is offset by dollar-for-dollar volatility in $B'$.  
Risk is fully conserved and reallocated.

\section{Transparency, Oracle Integrity, and Auditability}

All state variables $(V_A,V_B,\beta_t,P_0,v_t,H_u,H_d,T)$ are public on-chain.  
The \textbf{PriceFeed Contract} aggregates $P_t$ from multiple sources via median or TWAP filters.

Total ETH collateral $C_t$ and total liabilities:
\begin{equation}
L_t = N_A V_A(t) + N_B V_B(t),
\end{equation}
(where $N_A,N_B$ are outstanding tokens) must satisfy the solvency invariant:
\begin{equation}
C_t P_t \ge L_t.
\end{equation}
This inequality can be verified at any block.The resulting distribution of collateral value across senior and junior liabilities
is illustrated in Figure~\ref{fig:waterfall}.  
Each transition (payout, reset, or liquidation) corresponds to a rebalancing step
that preserves the on-chain solvency invariant.
\begin{figure}[H]
    \centering
    \includegraphics[width=1\linewidth]{Collateral Waterfall Diagram (1).png}
    \caption{Collateral waterfall under normal operation and in liquidation: priority of claims and residual distribution.}
    \label{fig:waterfall}
\end{figure}

\section{Economic Equilibrium and Endogenous Stability}

Conventional custodial stablecoins rely on external arbitrage, but
\textbf{Klages-Mundt (2021)} shows that such arbitrage cannot guarantee stability under endogenous leverage.  
In the dual-tranche model, stabilization is \textbf{internalized}:
\begin{itemize}
  \item Rising ETH $\Rightarrow V_B \uparrow \Rightarrow$ upward reset $\Rightarrow$ profit distribution $\Rightarrow$ leverage recentered.
  \item Falling ETH $\Rightarrow V_B \downarrow \Rightarrow$ downward reset $\Rightarrow$ recapitalization $\Rightarrow$ bounded risk.
\end{itemize}

Both $V_A$ and $V_B$ remain within $(H_d,H_u)$; equilibrium stability arises from deterministic arithmetic, not discretionary policy.

\section{Conclusion}

A stablecoin backed by a volatile crypto reserve can be \emph{mathematically stable} if volatility is partitioned rather than suppressed.  
The dual-tranche framework of Cao et al. (2023) encodes this principle explicitly through:
\begin{itemize}
  \item deterministic NAV equations,
  \item automatic upward and downward resets, and
  \item optional secondary splitting into $A′$ and $B′$.
\end{itemize}
Together, these components form a closed, autonomous, and fully auditable smart-contract system where stability is not promised---\textbf{it is computed.}

\newpage
\section*{References}
\begin{itemize}
\item Cao, Y., Dai, M., Kou, S., Li, L., \& Yang, C. (2023). \textit{Designing Stablecoins.} arXiv:2301.09288.
\item Klages-Mundt, A. (2021). \textit{While Stability Lasts: A Stochastic Model of Stablecoins.} arXiv:2109.10961.
\item Milionis, J., \& Huberman, G. (2023). \textit{The Design Space of Stablecoins.} SSRN 4374737.
\item MakerDAO Foundation (2021). \textit{The DAI Credit System Whitepaper.}
\item Adams, A. T. and Clunie, J. B. (2006).. \textit{Risk assessment techniques for split capital investment trusts. Annals of Actuarial Science, 1:7–36.}

\end{itemize}

\end{document}
