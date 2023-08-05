def write_optuna_analyse_script(path, input_branch_name):
    analyse_script = """{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import dvc_cc\n",
    "import dvc_cc.run\n",
    "dvc_cc.version.VERSION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess\n",
    "import json\n",
    "import numpy as np\n",
    "import optuna\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from pathlib import Path\n",
    "import optuna\n",
    "study = optuna.create_study(direction='minimize',\n",
    "                            study_name='study_1', \n",
    "                            storage='sqlite:///"""+input_branch_name+""".db?timeout=99999',\n",
    "                            load_if_exists=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "trial = study.best_trial\n",
    "\n",
    "print('Accuracy: {}'.format(trial.value))\n",
    "print(\"Best hyperparameters: {}\".format(trial.params))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.DataFrame(study.trials_dataframe())\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.groupby('state').count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "optuna.visualization.plot_optimization_history(study)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "optuna.visualization.plot_slice(study)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#optuna.visualization.plot_contour(study)#, params=['n_estimators', 'max_depth'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "optuna.visualization.plot_contour(study, params=['learning_rate', 'model_kernels'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "dvc-cc",
   "language": "python",
   "name": "dvc-cc"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}"""
    with open(path,'w') as f:
        print(analyse_script, file=f)

def write_optuna_execution_script(path, inputs, input_branch_name, jobs, num_of_trials):
    with open(path,'w') as f:

        print('# !/usr/bin/env python', file=f)
        print('# coding: utf-8', file=f)
        print('', file=f)

        print('def run_experiment(trial):', file=f)
        print('    from dvc_cc.hyperopt.variable import VariableCache', file=f)
        print('    import numpy as np', file=f)
        print('    import time', file=f)
        print('    vc = VariableCache()', file=f)
        print("    list_of_hyperopt_files = [f for f in os.listdir(str(Path('dvc/.hyperopt'))) if f.endswith('.hyperopt')]", file=f)
        print('    for f in list_of_hyperopt_files:', file=f)
        print("        f = str(Path('dvc/.hyperopt/' + f))", file=f)
        print('        vc.register_dvccc_file(f)', file=f)
        print('', file=f)

        print('    values = []', file=f)
        for k in inputs:
            t,v = inputs[k]
            if v.find('-') > 0:
                if t == 'float':
                    print('    values.append(trial.suggest_uniform("'+k+'", '+v[:v.find('-')]+','+v[v.find('-')+1:]+')'+')', file=f)
                else:
                    print('    values.append(trial.suggest_int("'+k+'", '+v[:v.find('-')]+','+v[v.find('-')+1:]+')'+')', file=f)
            elif v.find(',') > 0:
                print('    values.append(trial.suggest_categorical("'+k+'", ['+v+'])'
                      +')', file=f)
            else:
                print('    values.append('+v+') # ' + k, file=f)

        print("    result_branch = '"+input_branch_name+"_'+str(time.time_ns())", file=f)
        print("    dvc_save_path = 'dvc/' + result_branch", file=f)
        print('    os.mkdir(dvc_save_path)', file=f)
        print('    vc.set_values_for_hyperopt_files(values, dvc_save_path=dvc_save_path)', file=f)
        print('', file=f)
        print('    # Create RED-YMLnano', file=f)
        print("    with open('cc_execution_file_optuna.red.yml','r') as f:", file=f)
        print('        red_yml = f.read()', file=f)
        print("    red_yml = red_yml.replace('rcc_0032_MetricTest_XXXXXXXXXX', result_branch)", file=f)
        print("    with open(dvc_save_path+'/cc_execution_file.red.yml','w') as f:", file=f)
        print('        print(red_yml, file=f)', file=f)
        print('', file=f)
        print("    subprocess.call(('git add '+dvc_save_path+'/*').split(' '))", file=f)
        print('    subprocess.call("git commit -m \'SOMETHING\'".split(\' \'))', file=f)
        print('    subprocess.call("git push".split(\' \'))', file=f)
        print('', file=f)
        print('    # START RUN', file=f)
        print("    p = 'faice exec '+dvc_save_path+'/cc_execution_file.red.yml'# --disable-retry'", file=f)
        print("    message = subprocess.call(p.split(' '))", file=f)
        print('    result = None', file=f)
        print('    while result is None:', file=f)
        print('        time.sleep(np.random.randint(60))', file=f)
        print("        with open('metrics.json', 'r') as f:", file=f)
        print('            metrics = json.load(f)', file=f)
        print("        metrics = {m[:m.find('__')]:metrics[m] for m in metrics}", file=f)
        print('        if result_branch in metrics:', file=f)
        print('            result = metrics[result_branch]', file=f)
        print('', file=f)
        print('    return result', file=f)
        print('', file=f)
        print('import optuna', file=f)
        print('', file=f)
        print("study = optuna.create_study(direction='minimize',", file=f)
        print("                            study_name='study_1', ", file=f)
        print("                            storage='sqlite:///"+input_branch_name+".db?timeout=99999',", file=f)
        print('                            load_if_exists=True', file=f)
        print('                           )', file=f)
        print('', file=f)
        print('study.optimize(startbla, n_trials='+str(num_of_trials)+',n_jobs='+str(jobs)+')', file=f)


# parameters
#metric_path = 'loss.metric'
#input_branch = 'cc_0032_MetricTest'
#save_summary = '../learn-subjectivity/metrics.json'
def write_metric_getter_script(path, input_branch_name, metric_path, save_summary):
    with open(path,'w') as f:
        print('# !/usr/bin/env python', file=f)
        print('# coding: utf-8', file=f)
        print('', file=f)
        print('import git\nimport json\nimport os\nimport time\n', file=f)
        print('', file=f)
        print('g = git.Git()', file=f)
        print('', file=f)
        print("metric_path = '"+metric_path+"'", file=f)
        print("input_branch = '"+input_branch_name+"'", file=f)
        print("save_summary = '" + save_summary + "'", file=f)
        print('', file=f)
        print('metrics = {}', file=f)
        print('if not os.path.isfile(save_summary):', file=f)
        print("    with open(save_summary, 'w') as f:", file=f)
        print('        json.dump(metrics, f)', file=f)
        print('else:', file=f)
        print("    with open(save_summary, 'r') as f:", file=f)
        print('        metrics = json.load(f)', file=f)
        print('', file=f)
        print('while True:', file=f)
        print('    g.pull()', file=f)
        print('    time.sleep(1)', file=f)
        print("    all_branches = [b.split('/')[-1] for b in g.branch('-a').split() if", file=f)
        print("                    b.startswith('remotes/origin/r' + input_branch)]", file=f)
        print('    new_branches = [b for b in all_branches if b not in metrics.keys()]', file=f)
        print('    for b in new_branches:', file=f)
        print('        g.checkout(b)', file=f)
        print("        with open(metric_path, 'r') as f:", file=f)
        print('            metrics[b] = float(f.read())', file=f)
        print("    with open(save_summary, 'w') as f:", file=f)
        print('        json.dump(metrics, f)', file=f)
        print('    if len(new_branches):', file=f)
        print("        print('New-Branches: ', new_branches)", file=f)
        print('', file=f)


def setting_batch_concurrency_limit():
    from pathlib import Path
    import yaml

    with open(str(Path(".dvc_cc/cc_config.yml")), 'r') as stream:
        settings = yaml.safe_load(stream)

    return settings['execution']['settings']['batchConcurrencyLimit']


def create_optuna_directories(input_branch_name, vc):
    # 1. copy current directory
    import os
    import shutil
    jobstarter_path = '../'+os.getcwd().split('/')[-1]+'_'+input_branch_name.split('_')[1]+'_JobStarter'
    shutil.copytree('.', jobstarter_path)

    metric_path = '../' + os.getcwd().split('/')[-1] + '_MetricGetter'
    if not os.path.exists(metric_path):
        shutil.copytree('.', metric_path)

    # 2. get input values
    inputs = {}
    for v in vc.list_of_all_variables:
        inp = input(str(v.varname + ' (' + v.vartype + '): '))
        inputs[v.varname] = [v.vartype, inp]

    bcl = setting_batch_concurrency_limit()
    print()
    print('It is possible that ' + str(bcl) + ' (Batch Concurrency Limit) jobs can run in parallel.')
    num_of_trials = input('How many trials do you want?: ')


    # 3. Create optuna script,
    write_optuna_execution_script(path=jobstarter_path+'/run_optuna.py',inputs=inputs, input_branch_name=input_branch_name, jobs=bcl, num_of_trials=num_of_trials)
    # 4. analyse script
    write_optuna_analyse_script(jobstarter_path+'/analyse_optuna.ipynb', input_branch_name)

    # 5. Create metrics getter script
    # TODO: The 'loss.metric' must be a variable !
    write_metric_getter_script(metric_path + '/get_metrics.py', input_branch_name,
                               'loss.metric', jobstarter_path+'/metrics.json')

