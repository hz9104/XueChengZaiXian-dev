import math, os, sys, json

#此脚本的目的是为纯净版主脚本添加魔改功能，只要主脚本结构不大改，理论上可应对之后所有的更新版本
#自己备份主脚本文件
#自己改文件路径，变量名为file_path,注意反斜杠要使用双反斜杠，参考我的写法
#不想要的功能可以整段注释掉
#不会弄就别弄，总有明白人弄好了上传群文件的

"""以下为时间戳"""
target_text1 ="            mutation: \"突变\","
text_to_insert1 = "\n        },\n \n	logTime(){\n		let nowdate = new Date();\n		let timetext = nowdate.toTimeString().split(' ')[0];\n		return `[`+timetext+`] [${game.global.stats.days}] `;"

file_path = 'C:\\Users\\username\\Desktop\\script\\3.3.1.108.11.txt'

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if target_text1 in lines[i]:
        lines[i] = lines[i].replace(target_text1, target_text1 + text_to_insert1)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

target_text2 = "poly.messageQueue("
text_to_insert2 = "GameLog.logTime() + "

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for j in range(len(lines)):
    if target_text2 in lines[j]:
        lines[j] = lines[j].replace(target_text2, target_text2 + text_to_insert2)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

print("已成功添加时间戳")

"""以上为时间戳"""

"""以下为总督"""
target_text3 = "            GameLog.logSuccess(\"mercenary\", `雇佣了 ${mercenariesHired} 名雇佣兵。`, ['combat']);"
text_to_insert3 = '''\n
        }
    }
    function autoFire() {
        if (haveTech("governor") && settings.govGovernor !== "none" && getGovernor() !== "none") {
            let govOffice = (()=>{try{return document.getElementById("govOffice").__vue__}catch(e){return undefined}})();
            if (game.global.race.governor?.g?.bg !== settings.govGovernor){
                govOffice.fire();
                return;
            }
'''

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for k in range(len(lines)):
    if target_text3 in lines[k]:
        lines[k] = lines[k].replace(target_text3, target_text3 + text_to_insert3)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

target_text4 = "        return (30 + (amount - 1) * 2.5) * amount * (game.global.race['emfield'] ? 1.5 : 1);"
text_to_insert4 = '''\n
    }

    function resetAutoFire(reset) {
        let def = {
            autoFire: false,
        }
        applySettings(def, reset);
'''

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for l in range(len(lines)):
    if target_text4 in lines[l]:
        lines[l] = lines[l].replace(target_text4, target_text4 + text_to_insert4)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

target_text5 = "            autoJobs(true);"
text_to_insert5 = '''\n
        }

        if (settings.autoFire) {
            autoFire();
'''

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for m in range(len(lines)):
    if target_text5 in lines[m]:
        lines[m] = lines[m].replace(target_text5, target_text5 + text_to_insert5)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

target_text6 = "            createSettingToggle(togglesNode, 'autoResearch', '自动研究', '当满足相应条件时自动进行研究。');"
text_to_insert6 = "\n            createSettingToggle(togglesNode, 'autoFire', '自动解雇总督', '当当前总督不符合设置时自动进行替换。');"

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for n in range(len(lines)):
    if target_text6 in lines[n]:
        lines[n] = lines[n].replace(target_text6, target_text6 + text_to_insert6)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

print("已成功添加自动换总督")

"""以上为总督"""

"""以下为复制器电量"""
target_text7 = "            getVueById(\"govOffice\").setTask('replicate', replicatorTaskIndex);"
text_to_insert7 = '''\n
        }
        
        //以下为添加内容
        let inputEvent = new Event('input');
        //最大电力设置
        if (game.global.race.governor.config.replicate.pow.cap != 2000000) {
            let repConfigPowCap = document.querySelectorAll(".tConfig")[8].querySelectorAll(".storage")[0].querySelectorAll(".b-numberinput input")[0];
            repConfigPowCap.value = 2000000; //设置“至多使用电力”
            repConfigPowCap.dispatchEvent(inputEvent);
        }

        let buildingList = [...BuildingManager.managedPriorityList(), ...ProjectManager.managedPriorityList()].sort((a, b) => b.weighting - a.weighting);
        //电力缓冲值设置
        let repConfigPowBuffer = document.querySelectorAll(".tConfig")[8].querySelectorAll(".storage")[0].querySelectorAll(".b-numberinput input")[1];
        let powerBuffer = 5;
        for (let unlockedBuilding of buildingList) {
            if (unlockedBuilding.powered > powerBuffer) {
                powerBuffer = unlockedBuilding.powered;
            }
            repConfigPowBuffer.value = Math.ceil(powerBuffer * 1); //设置“可用电力缓冲值”，为可建造建筑最大耗电量的5倍（倍率可自行修改）
            repConfigPowBuffer.dispatchEvent(inputEvent);
            //以上为添加内容
'''

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for o in range(len(lines)):
    if target_text7 in lines[o]:
        lines[o] = lines[o].replace(target_text7, target_text7 + text_to_insert7)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

print("已成功添加总督控制电量")

"""以上为复制器电量"""

"""以下为智械阋神星和马蹄检测"""
target_text8 = "        // Reset required storage and prioritized resources"
text_to_insert8 = '''\n
        if (state.goal === "Standard" && evolve.global.stats.days <= 10)
        {
            try {
                if (evolve.global.space.position.spc_eris > 270
                    || evolve.global.space.position.spc_eris < 90) {
                        GameLog.logDanger("special", `糟糕，阋神星太远了，位置：`+evolve.global.space.position.spc_eris, ['progress']);
                        let resetButton = document.querySelector(".reset .button:not(.right)");
                        if (resetButton.innerText === game.loc("reset_soft")) {
                            if (settings.evolutionQueueEnabled && settingsRaw.evolutionQueue.length > 0) {
                                if (!settings.evolutionQueueRepeat) {
                                    addEvolutionSetting();
                                }
                                settingsRaw.evolutionQueue.unshift(settingsRaw.evolutionQueue.pop());
                            }
                            updateSettingsFromState();

                            state.goal = "GameOverMan";
                            resetButton.disabled = false;
                            resetButton.click();
                        }
                }
            } catch (error) {
            }
        }
        if (state.goal === "Standard" && evolve.global.stats.days <= 10)
        {
            try {
                if (evolve.global.race.hooved> 0 && game.global.race['truepath']) {
                        GameLog.logDanger("special", `糟糕，我们遇到马蹄了`, ['progress']);
                        let resetButton = document.querySelector(".reset .button:not(.right)");
                        if (resetButton.innerText === game.loc("reset_soft")) {
                            if (settings.evolutionQueueEnabled && settingsRaw.evolutionQueue.length > 0) {
                                if (!settings.evolutionQueueRepeat) {
                                    addEvolutionSetting();
                                }
                                settingsRaw.evolutionQueue.unshift(settingsRaw.evolutionQueue.pop());
                            }
                            updateSettingsFromState();

                            state.goal = "GameOverMan";
                            resetButton.disabled = false;
                            resetButton.click();
                        }
                }
            } catch (error) {
            }
        }

'''
with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for p in range(len(lines)):
    if target_text8 in lines[p]:
        lines[p] = lines[p].replace(target_text8, target_text8 + text_to_insert8)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

print("已成功添加智械智能软重置")

"""以上为智械阋神星和马蹄检测"""

"""以下为血湖后建筑权重控制"""
target_text9 = "          () => 1 + Math.random() // Fluctuate weight to pick random item"
text_to_insert9 = '''\n
      ],[
          () => haveTech("sphinx_bribe", 1),
          (building) => building._tab === "city" || building._tab === "space" || building._tab === "interstellar",
          () => "血湖前建筑",
          () => settings.buildingWeightingAfterLake
'''

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for q in range(len(lines)):
    if target_text9 in lines[q]:
        lines[q] = lines[q].replace(target_text9, target_text9 + text_to_insert9)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

target_text10 = "            buildingWeightingOverlord: 0,"
text_to_insert10 = "\n            buildingWeightingAfterLake: 1,"

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for r in range(len(lines)):
    if target_text10 in lines[r]:
        lines[r] = lines[r].replace(target_text10, target_text10 + text_to_insert10)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

target_text11 = "        addWeightingRule(tableBodyNode, \"众鼬任务\", \"与主宰成就冲突的接触众鼬选项\", \"buildingWeightingOverlord\");"
text_to_insert11 = "\n        addWeightingRule(tableBodyNode, \"血湖后建筑权重\", \"到达血湖之后的地面、星系、星际建筑\", \"buildingWeightingAfterLake\");"

with open(file_path, 'r', encoding = "utf-8") as f:
    lines = f.readlines()

for s in range(len(lines)):
    if target_text11 in lines[s]:
        lines[s] = lines[s].replace(target_text11, target_text11 + text_to_insert11)

with open(file_path, 'w', encoding = "utf-8") as f:
    f.writelines(lines)

print("已成功添加血湖后权重控制")

"""以上为血湖后建筑权重控制"""