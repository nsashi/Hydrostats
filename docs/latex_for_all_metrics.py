import sympy as sp

metric_abbr = [
    'ME', 'MAE', 'MSE', 'MLE', 'MALE', 'MSLE', 'MdE', 'MdAE', 'MdSE', 'ED', 'NED', 'RMSE', 'RMSLE',
    'NRMSE (Range)', 'NRMSE (Mean)', 'NRMSE (IQR)', 'IRMSE', 'MASE', 'r2', 'R (Pearson)',
    'R (Spearman)', 'ACC', 'MAPE', 'MAPD', 'MAAPE', 'SMAPE1', 'SMAPE2', 'd', 'd1', 'd (Mod.)',
    'd (Rel.)', 'dr', 'M', '(MB) R', 'NSE', 'NSE (Mod.)', 'NSE (Rel.)', 'KGE (2009)', 'KGE (2012)',
    "E1'", "D1'", 'VE', 'SA', 'SC', 'SID', 'SGA', 'H1 (MHE)', 'H1 (AHE)', 'H1 (RMSHE)', 'H2 (MHE)',
    'H2 (AHE)', 'H2 (RMSHE)', 'H3 (MHE)', 'H3 (AHE)', 'H3 (RMSHE)', 'H4 (MHE)', 'H4 (AHE)',
    'H4 (RMSHE)', 'H5 (MHE)', 'H5 (AHE)', 'H5 (RMSHE)', 'H6 (MHE)', 'H6 (AHE)', 'H6 (RMSHE)',
    'H7 (MHE)', 'H7 (AHE)', 'H7 (RMSHE)', 'H8 (MHE)', 'H8 (AHE)', 'H8 (RMSHE)', 'H10 (MHE)',
    'H10 (AHE)', 'H10 (RMSHE)', 'GMD', 'MV'
]

latex_symbols = {
    'ME': r'$ME = \frac{1}{n} \sum_{i=0}^{n} (S_i - O_i)$',
    'MAE': r'$MAE = \frac{1}{n} \sum_{i=0}^{n} | S_i - O_i |$',
    'MSE': r'$MSE = \frac{1}{n} \sum_{i=1}^{n}(S_i - O_i)^2$',
    'MLE': r'$MLE = \frac{1}{n} \sum_{i=0}^{n} ln(\frac{S_i}{O_i})$',
    'MALE': r'$MALE = \frac{1}{n} \sum_{i=0}^{n} | ln(\frac{S_i}{O_i}) |$',
    'MSLE': r'$MALE = \frac{1}{n} \sum_{i=0}^{n} (ln(\frac{S_i}{O_i}))^2$',
    'MdE': r'$MdE = median(S_i - O_i)$',
    'MdAE': r'$MdE = median|S_i - O_i|$',
    'MdSE': r'$MdE = median(S_i - O_i)^2$',
    'ED': r'$ED = (\sum_{i=0}^{n}|S_i-O_i|^2)^\frac{1}{2}$',
    'NED': r'$NED = (\sum_{i=0}^{n}|\frac{S_i}{\overline{S}}-\frac{O_i}{\overline{O}}|^2)^'
           r'\frac{1}{2}$',
    'RMSE': r'$RMSE = (\frac{1}{n} \sum_{i=0}^{n}(S_i-O_i)^2)^\frac{1}{2}$',
    'RMSLE': r'$RMSLE = (\frac{1}{n} \sum_{i=0}^{n}(ln(\frac{S_i}{O_i}))^2)^\frac{1}{2}$',
    'NRMSE_Range': r'$NRMSE_{Range} = \frac{RMSE}{O_{max} - O_{min}}$',
    'NRMSE_Mean': r'$NRMSE_{Mean} = \frac{RMSE}{\overline{O}}$',
    'NRMSE_IQR': r'$NRMSE_{quartile} = \frac{RMSE}{Quartile_3 - Quartile_1}$',
    'IRMSE1': r'$\Delta_O=(O_2 - O_1, O_3 - O_2, ... , O_n - O_{n-1})$',
    'IRMSE2': r'$\sigma_{\Delta_O}=\sqrt{\sum_{i=1}^{n}\frac{(\Delta_{O_i}-\overline{\Delta_O})^2}'
              r'{n-1}}=\text{std}(\Delta_O)$',
    'IRMSE3': r'$IRMSE = \frac{RMSE}{\sigma_{\Delta_O}}$',
    'MASE': r'$MASE = \frac{\sum_{i=1}^{n}|S_i-O_i|}{\frac{n}{n-1}\sum_{i=1}^{n}|O_i-O_{i-1}|}$',
    'r2': r'$R^2=\frac{(\sum_{i=1}^{n}(O_i-\overline{O})(S_i-\overline{S}))^2}'
          r'{\sum_{i=1}^{n}(O_i-\overline{O})^2\sum_{i=1}^{n}(S_i-\overline{S})^2}$',
    'R_pearson': r'$R_{Pearson}=\frac{\sum_{i=1}^{n}(O_i-\overline{O})(S_i-\overline{S})}{\sqrt{'
                 r'\sum_{i=1}^{n}(O_i-\overline{O})^2}\sqrt{\sum_{i=1}^{n}(S_i-\overline{S})^2}}$',
    'R_spearman': r'$R_{Spearman}=\frac{\frac{1}{n}\sum_{i=1}^{n}(R(O_i)-\overline{R(O)})(R(S_i)-'
                  r'\overline{R(S)})}{\sqrt{\frac{1}{n}\sum_{i=1}^{n}(R(O_i)-\overline{R(O)})^2}'
                  r'\sqrt{\frac{1}{n}\sum_{i=1}^{n}(R(S_i)-\overline{R(S)})^2}}$',
    'ACC': r'$ACC=\frac{1}{n}\frac{\sum_{i=1}^{n}(S_i-\overline{S})(O_i-\overline{O})}{\sigma_o'
           r'\sigma_s}$',
    'MAPE': r'$MAPE=\frac{100\%}{n}\sum_{i=1}^{n}|\frac{S_i-O_i}{O_i}|$',
    'MAPD': r'$MAPE=100\%\frac{\sum_{i=1}^{n}|S_i-O_i|}{\sum_{i=1}^{n}|O_i|}$',
    'MAAPE': r'$MAPE=\frac{1}{n}\sum_{i=1}^{n}arctan|\frac{S_i-O_i}{O_i}|$',
    'SMAPE1': r'$sMAPE1=\frac{100\%}{n}\sum_{i=1}^{n}\frac{|S_i-O_i|}{|S_i|+|O_i|}$',
    'SMAPE2': r'$sMAPE1=\frac{100\%}{n}\sum_{i=1}^{n}|\frac{S_i-O_i}{\frac{(S_i+O_i)}{2}}|$',
    'd': r'$d=1-\frac{\sum_{i=1}^{n}(S_i-O_i)^2}{\sum_{i=1}^{n}(|S_i-\overline{O}|+|O_i-'
         r'\overline{O}|)^2}$',
    'd1': r'$d_{1}=1-\frac{\sum_{i=1}^{n}|S_i-O_i|}{\sum_{i=1}^{n}(|S_i-\overline{O}|+|O_i-'
          r'\overline{O}|)}$',
    'dmod': r'$d_{mod}=1-\frac{\sum_{i=1}^{n}|S_i-O_i|^j}{\sum_{i=1}^{n}(|S_i-\overline{O}|+|O_i-'
            r'\overline{O}|)^j}$',
    'drel': r'$d_{rel}=1-\frac{\sum_{i=1}^{n}(\frac{S_i-O_i}{O_i})^2}{\sum_{i=1}^{n}(\frac{|S_i-'
            r'\overline{O}|+|O_i-\overline{O}|}{\overline{O}})^2}$',
    'dr1': r'$Note: \enspace ||S_i-O_i||=\sum_{i=1}^n|S_i-O_i|$',
    'dr2': r'$when \enspace ||S_i-O_i|| \leq 2||O_i-\overline{O}||, \enspace d_r=1-\frac{||S_i-O_i|'
           r'|}{2||O_i-\overline{O}||}$',
    'dr3': r'$when \enspace ||S_i-O_i|| > 2||O_i-\overline{O}||, \enspace d_r=\frac{2||O_i-'
           r'\overline{O}||}{||S_i-O_i||}-1$',
    'M': r'$M=\left(\frac{2}{\pi}\right)sin^{-1}\left(1-\frac{MSE}{\sigma^2_s+\sigma^2_o+'
         r'(\overline{S}-\overline{O})^2}\right)$',
    'MB_R': r'$\Re=1-\frac{MAE}{n^{-2}\sum_{j=1}^{n}\sum_{i=1}^{n}|S_j-O_i|}$',
    'NSE': r'$NSE=1-\frac{\sum_{i=1}^{n}(S_i-O_i)^2}{\sum_{i=1}^{n}(O_i-\overline{O})^2}$',
    'NSEmod': r'$NSE_{mod}=1-\frac{\sum_{i=1}^{n}|S_i-O_i|^j}{\sum_{i=1}^{n}|O_i-\overline{O}|^j}$',
    'NSErel': r'$NSE_{rel}=1-\frac{\sum_{i=1}^{n}\left|\frac{S_i-O_i}{O_i}\right|^2}{\sum_{i=1}^{n}'
              r'\left|\frac{O_i-\overline{O}}{\overline{O}}\right|^2}$',
    'KGE_2009_1': r'$KGE_{2009}=1-ED$',
    'KGE_2009_2': r'$ED=\sqrt{(s[1]*(r-1))^2+(s[2]*(\alpha-1))^2+(s[3]*(\beta-1))^2}$',
    'KGE_2009_3': r'$r = Pearson \enspace Correlation \enspace Coefficient$',
    'KGE_2009_4': r'$\beta=\mu_s / \mu_o$',
    'KGE_2009_5': r'$\alpha = \sigma_s / \sigma_o$',
    'KGE_2012_1': r'$KGE_{2012}=1-ED$',
    'KGE_2012_2': r'$ED=\sqrt{(s[1]*(r-1))^2+(s[2]*(\gamma-1))^2+(s[3]*(\beta-1))^2}$',
    'KGE_2012_3': r'$r = Pearson \enspace Correlation \enspace Coefficient$',
    'KGE_2012_4': r'$\beta=\mu_s / \mu_o$',
    'KGE_2012_5': r'$\gamma = \frac{CV_s}{CV_o} = \frac{\sigma_s/\mu_s}{\sigma_o/\mu_o}$',
    'E1p': r"$E_{1}^{'} = 1-\frac{\sum_{i=1}^{n}\left|S_i-O_i\right|}{\sum_{i=1}^{n} \left|O_i-"
           r"\overline{O_i^{'}}\right|}$",
    'D1p': r"$d_{1}^{'} = 1-\frac{\sum_{i=1}^{n}\left|S_i-O_i\right|}{\sum_{i=1}^{n} \left| S_i - \overline{O_i^{'}} "
           r"\right| + \left| O_i - \overline{O_i^{'}} \right| }$",
    'VE': r'$VE = 1-\frac{\sum_{i=1}^{n} |S_i - O_i|}{\sum_{i=1}^{n} O_i}$',
    'SA': r"$SA = arccos\left( \frac{\langle S, O \rangle}{||S||^{}_2 ||O||^{}_2} \right)$",
    'SC': r'$SC = arccos\left(\frac{\langle(S_i-\overline{S})(O_i-\overline{O})\rangle}{||S_i-'
          r'\overline{S}||_2 ||O_i-\overline{O}||_2}\right)$',
    'SID': r'$\Biggl\langle \left( \frac{O_i}{\overline{O}} - \frac{S_i}{\overline{S}} \right), '
           r'\left( log \left( \frac{O_i}{\overline{O}} \right) - log \left( \frac{S_i}'
           r'{\overline{S}} \right) \right)  \Biggr\rangle$',
    'SGA1': r'$SG_o = (O_2-O_1, O_3-O_2,...,O_n-O_{n-1})$',
    'SGA2': r'$SG_s = (S_2-S_1, S_3-S_2,...,S_n-S_{n-1})$',
    'SGA3': r'$SGA = SA(SG_o, SG_s)$',
    'SGA4': r'$Note: SA=Spectral \enspace Angle \enspace Metric$',
    'MHE': r'$\text{Mean H Error} =\frac {1}{n}\sum_{i=1}^{n} H$',
    'AHE': r'$\text{Absolute H Error} =\frac {1}{n}\sum_{i=1}^{n} |H|$',
    'RMSHE': r'$\text{Root Mean Squared H Error} = \sqrt{\frac {1}{n}\sum_{i=1}^{n} H^2}$',
    'H1': r'$H_1 = \frac {S_i-O_i}{O_i}$',
    'H2': r'$H_2 = \frac {S_i-O_i}{S_i}$',
    'H3': r'$H_3 = \frac {S_i-O_i}{\frac{1}{2}(S_i+O_i)}$',
    'H4': r'$H_4 = \frac {S_i-O_i}{\sqrt{S_iO_i}}$',
    'H5': r'$H_5 = \frac{S_i - O_i}{\left [ \frac {1}{2} \left ( O_i^{-1} + S_i^{-1} \right ) '
          r'\right ]^{-1}}$',
    'H6': r'$H_6 = \frac{S_i - O_i}{\left [ \frac {1}{2} \left ( O_i^{k} + S_i^{k} \right ) '
          r'\right ]^{1/k}}$',
    'H7': r'$H_7 = \frac {S_i - O_i}{min(O_i,S_i)}$',
    'H8': r'$H_8 = \frac {S_i - O_i}{max(O_i,S_i)}$',
    'H10': r'$H_{10} = \ln{ \frac {S_i}{O_i}}$',
    'GMD': r'$\text{GM} = e^{\left(\sqrt[n]{\ln(S_1)\ln(S_2)\cdot\cdot\cdot \ln(S_n)} - \sqrt[n]'
           r'{\ln(O_1)\ln(O_2)\cdot\cdot\cdot \ln(O_n)}\right)}$',
    'MV': r'$\text{MV} = \text{var}(\ln(O_1), \ln(O_2),..., \ln(O_n) - \text{var}(\ln(S_1), '
          r'\ln(S_2),..., \ln(S_n)$'
}

all_metrics = list(latex_symbols.keys())
all_metrics.sort()
for metric in all_metrics:
    print(metric)
    sp.preview(latex_symbols[metric], viewer='file',
               filename='/home/wade/Hydrostats/docs/New_Files/{}.png'.format(metric))


# sp.preview(, viewer='file', filename="test.png", euler=True)

