<details>
<summary>Click to view research outputs</summary>
<div class="details-body">

<!-- Research Experience -->
<div class="section-header">
  <h2> Research Experience</h2>
</div>

<div class="research-section">
<h3 class="subsection-title"> Publications & Academic Projects</h3>

<div class="publication-item">
  <div class="publication-figure" data-badge="IP&M">
    <img src="static/assets/img/research/paper1.svg" alt="Multi-Source Mixed-Frequency Interval-Valued Crude Oil Price Forecasting">
  </div>
  <div class="publication-content">
    <div class="publication-title">
      <a href="#">What Can Be Learned from Multi-Source Mixed-Frequency Interval-Valued Information? Evidence from a Context-Aware Dynamic Ensemble Interval-Valued Crude Oil Price Forecasting System</a>
    </div>
    <div class="publication-authors">Second Author (Advisor as First Author)</div>
    <div class="publication-meta">
      <span>Journal: Information Processing & Management (IP&M, CCF-B)</span>
      <span>Status: Under Revision (1st Round)</span>
      <span>Duration: 2025.03 ~ 2025.11</span>
    </div>
    <div class="publication-links">
      <a href="#">PDF</a>
      <details class="publication-abstract">
        <summary>Research Details</summary>
        <div class="details-body">
          <p><strong>Research Problem:</strong> Existing time-series models struggle to effectively fuse cross-scale dependencies in multi-source mixed-frequency data, and static ensemble strategies are sensitive to data distribution drift.</p>
          <ul class="publication-notes">
            <li><strong>Multi-Stage Feature Engineering:</strong> Designed a feature selection and compression module integrating 11 ML algorithms, performing low-rank compression to alleviate over-parameterization.</li>
            <li><strong>Multi-Source Mixed-Frequency Modeling (M-MIDAS):</strong> Proposed a heterogeneous feature processing method applying parameterized polynomial lag mappings to different frequency sequences, constructing low-dimensional vectors that fuse multi-source information at each time step, achieving structured cross-scale fusion through learnable aggregation layers.</li>
            <li><strong>Dual-Attention Dynamic Ensemble:</strong> Constructed a dynamic ensemble module with parallel variable and temporal attention branches at the Transformer encoder end, enabling adaptive ensemble weights that automatically enhance robust model contributions in high-variance intervals with interpretability.</li>
            <li><strong>Experimental Results:</strong> Achieved approximately 23.6% performance improvement over mainstream SOTA models on WTI and Brent datasets.</li>
          </ul>
        </div>
      </details>
    </div>
  </div>
</div>

<div class="publication-item">
  <div class="publication-figure" data-badge="Systems">
    <img src="static/assets/img/research/paper2.svg" alt="Multi-Step Carbon Price Forecasting System">
  </div>
  <div class="publication-content">
    <div class="publication-title">
      <a href="#">A Multi-Step Interval-Valued Carbon Price Forecasting System Based on Multi-Source Mixed-Frequency Information Modeling</a>
    </div>
    <div class="publication-authors">First Author (Advisor as Corresponding Author)</div>
    <div class="publication-meta">
      <span>Journal: Systems (SCI)</span>
      <span>Status: Under Revision (1st Round)</span>
      <span>Duration: 2025.11 ~ 2026.03</span>
    </div>
    <div class="publication-links">
      <a href="#">PDF</a>
      <details class="publication-abstract">
        <summary>Research Details</summary>
        <div class="details-body">
          <p><strong>Research Problem:</strong> Multi-step time-series forecasting suffers from error accumulation and long-term dependency decay, while redundant variables in high-dimensional feature spaces exacerbate performance degradation in non-stationary scenarios.</p>
          <ul class="publication-notes">
            <li><strong>Dynamic Feature Selector:</strong> Proposed a multi-objective reinforcement learning-based dynamic feature selector that learns sparse filtering strategies using prediction error and feature set cardinality as joint reward signals.</li>
            <li><strong>Frequency-Aware Mixed-Frequency Representation:</strong> Constructed a frequency-aware mixed-frequency representation frontend that uses M-MIDAS to fuse and downsample high-dimensional heterogeneous data, outputting temporal representations for downstream deep learning model training.</li>
            <li><strong>Residual Dynamic Correction:</strong> Designed a residual-driven dynamic correction network that parallels a learnable residual compensation branch with the backbone predictor to suppress error propagation in multi-step inference.</li>
          </ul>
        </div>
      </details>
    </div>
  </div>
</div>

<div class="publication-item">
  <div class="publication-figure" data-badge="ES">
    <img src="static/assets/img/research/paper3.svg" alt="Green Metal Market Price Forecasting">
  </div>
  <div class="publication-content">
    <div class="publication-title">
      <a href="#">A New Multi-Objective Ensemble System for Geoscience Resource Price Forecasting: Evidence from the Green Metal Market</a>
    </div>
    <div class="publication-authors">Third Author</div>
    <div class="publication-meta">
      <span>Journal: Expert Systems (CCF-C)</span>
      <span>Status: Under Revision (2nd Round)</span>
      <span>Duration: 2024.12 ~ 2025.03</span>
    </div>
    <div class="publication-links">
      <a href="#">PDF</a>
      <details class="publication-abstract">
        <summary>Research Details</summary>
        <div class="details-body">
          <p>The system adopts a four-stage framework of sequence decomposition, adaptive predictor selection, multi-objective ensemble optimization, and final prediction generation.</p>
          <ul class="publication-notes">
            <li><strong>Personal Contribution:</strong> Responsible for the multi-objective ensemble optimization module, formalizing ensemble weight solving as a bi-objective optimization problem of accuracy and variance, using MOAOA to search for Pareto-optimal weight vectors, introducing adaptive grids to maintain frontier scale, and automatically selecting final weights based on minimum variance criteria.</li>
            <li><strong>Experimental Results:</strong> Effectively reduced overall performance metrics across three metal price datasets.</li>
          </ul>
        </div>
      </details>
    </div>
  </div>
</div>

<div class="publication-item">
  <div class="publication-figure" data-badge="NSFC">
    <img src="static/assets/img/research/paper6.svg" alt="Wind Power Forecasting Research">
  </div>
  <div class="publication-content">
    <div class="publication-title">
      <a href="#">Dynamic Adaptive Probabilistic Wind Power Forecasting Based on Mixed-Frequency Big Data</a>
    </div>
    <div class="publication-authors">Project Participant</div>
    <div class="publication-meta">
      <span>Project Type: National Natural Science Foundation of China</span>
      <span>Duration: 2024.01 ~ 2026.12</span>
    </div>
    <div class="publication-links">
      <details class="publication-abstract">
        <summary>Project Details</summary>
        <div class="details-body">
          <p><strong>Project Overview:</strong> Designed a three-stage framework of anomaly detection, data repair, and feature learning to achieve structured fusion and quality enhancement of multi-source heterogeneous spatiotemporal data.</p>
          <p><strong>My Work:</strong></p>
          <ul class="publication-notes">
            <li>Assisted in data cleaning, alignment, and spatiotemporal matching for four types of heterogeneous data to ensure input data quality.</li>
            <li>Participated in anomaly detection module data annotation and rule verification, assisting in multi-type anomaly sample identification based on physical constraints and statistical methods.</li>
            <li>Built Git experimental management repository to unify data versioning, script environments, and parameter configurations.</li>
            <li>Participated in data repair solution discussions combining graph structure modeling and generative models, assisting in missing data completion experiments based on spatial correlations between stations.</li>
            <li>Assisted in designing shallow feature screening modules, exploring the combination of voting mechanisms and multi-objective optimization in key variable selection.</li>
            <li>Participated in Transformer+TCN deep encoder multi-scale fusion strategy experiments, validating the impact of different fusion approaches on prediction accuracy.</li>
          </ul>
        </div>
      </details>
    </div>
  </div>
</div>

<div class="publication-item">
  <div class="publication-figure publication-figure--centered" data-badge="Open Source">
    <img src="static/assets/img/research/paper4.svg" alt="LLM Agent Time Series System">
  </div>
  <div class="publication-content">
    <div class="publication-title">
      <a href="https://github.com/Junyuan-Li/wind-power-llm-agent" target="_blank">Interpretable Time-Series Forecasting System Integrating RAG and Multi-Agent Framework</a>
    </div>
    <div class="publication-authors">Independent Development</div>
    <div class="publication-meta">
      <span>Duration: 2025.12 ~ 2026.02</span>
      <span>Code: <a href="https://github.com/Junyuan-Li/wind-power-llm-agent" target="_blank">GitHub Repository</a></span>
    </div>
    <div class="publication-links">
      <details class="publication-abstract">
        <summary>Project Details</summary>
        <div class="details-body">
          <ul class="publication-notes">
            <li><strong>Hierarchical RAG Mechanism:</strong> Introduced a hierarchical RAG mechanism, built historical meteorological pattern vector indices based on Text Embedding and FAISS, retrieving similar case mechanism descriptions as contextual prompts to integrate into the reasoning process.</li>
            <li><strong>Multi-Agent Collaboration:</strong> Designed a Planner-Executor-Writer multi-agent collaborative framework, decoupling task planning, prediction execution, and explanation generation to achieve chain-based collaboration.</li>
            <li><strong>LLM Fine-tuning & Deployment:</strong> Performed parameter-efficient fine-tuning on Qwen2.5-7B using QLoRA and deployed locally, built CLI and Web visualization interfaces to achieve interactive prediction and natural language explanation outputs.</li>
          </ul>
        </div>
      </details>
    </div>
  </div>
</div>

</div>
</details>


