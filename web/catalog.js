// Каталог: чистые функции поверх tasks.json и taskState, без DOM.
import { taskState } from "./unlock.js";

export const LANGS = [["python", "Python"], ["sql", "SQL"], ["ts", "TypeScript"], ["java", "Java"]];
export const LEVELS = [["easy", "Easy"], ["medium", "Medium"], ["hard", "Hard"]];
const LEVEL_RANK = { easy: 0, medium: 1, hard: 2 };

const byLevelOrder = (a, b) => LEVEL_RANK[a.level] - LEVEL_RANK[b.level] || a.order - b.order;

export function langCounts(tasks, solved) {
  const out = {};
  for (const [lang] of LANGS) {
    const own = tasks.filter(t => t.lang === lang);
    out[lang] = { solved: own.filter(t => solved.has(t.id)).length, total: own.length };
  }
  return out;
}

// Темы языка с задачами после фильтров. Без фильтра по теме — все темы (пустые тоже), с фильтром — только она.
export function catalog(tasks, topics, solved, { lang, topic, level }) {
  return (topics[lang] || [])
    .filter(tp => !topic || tp.id === topic)
    .map(tp => {
      const items = tasks.filter(t => t.lang === lang && t.topic === tp.id && (!level || t.level === level))
        .sort(byLevelOrder)
        .map(t => ({ task: t, state: taskState(t, tasks, solved) }));
      return { topic: tp, items, solved: items.filter(i => i.state === "solved").length };
    })
    .filter(c => !level || c.items.length);
}

// Следующая открытая задача темы: сперва после текущей (уровень, порядок), иначе любая открытая раньше.
export function nextTask(task, tasks, solved) {
  const topic = tasks.filter(t => t.lang === task.lang && t.topic === task.topic).sort(byLevelOrder);
  const i = topic.findIndex(t => t.id === task.id);
  const open = t => t.id !== task.id && taskState(t, tasks, solved) === "open";
  return topic.slice(i + 1).find(open) ?? topic.slice(0, Math.max(i, 0)).find(open) ?? null;
}

// Для закрытой задачи — та, что надо решить сначала: первая нерешённая в её цепочке.
export function blocker(task, tasks, solved) {
  return tasks.filter(t => t.lang === task.lang && t.topic === task.topic && t.level === task.level)
    .sort((a, b) => a.order - b.order)
    .find(t => !solved.has(t.id)) ?? null;
}
