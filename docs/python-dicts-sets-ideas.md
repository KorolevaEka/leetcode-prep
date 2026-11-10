# python / dicts-sets ideas (new tasks 05..30)

Relabel: 04 duplicate-users hard -> medium (normalise + group, no algorithm). Re-hint 01-04 per policy.

| NN | lvl | title / signature | rule + edges | technique | mutants |
|----|-----|-------------------|--------------|-----------|---------|
| 05 | easy | new_failures(previous, current) | names in current not in previous, order of current, once each; empty | set difference keeping order | sorted-result, keeps-duplicates |
| 06 | easy | merge_settings(defaults, overrides) | overrides win; None in overrides deletes key; inputs unchanged | dict merge | mutates-input, none-kept |
| 07 | easy | common_tags(suites) | tags present in every suite, sorted; [] -> [] | set intersection | union, crashes-on-empty |
| 08 | easy | missing_fields(response, required) | required fields absent or None, order of required (0/""/False are present) | membership / get | falsy-missing, ignores-none |
| 09 | easy | header_value(headers, name) | case-insensitive lookup; first match in dict order; None | key normalisation | case-sensitive, last-match |
| 10 | easy | diff_configs(old, new) | {"added","removed","changed"} sorted key lists | key set ops | no-changed, unsorted |
| 11 | easy | top_error(errors) | most frequent; tie -> first to appear; empty -> None | count + tie-break | tie-last, tie-alpha |
| 12 | easy | index_by_id(items) | id -> item, last duplicate wins, items without "id" skipped | dict build | first-wins, no-skip-missing |
| 13 | med | flaky_tests(runs) | runs [(name, passed)]; names with both outcomes, first-appearance order | dict of sets | needs-fail-first, includes-all-failed |
| 14 | med | find_pair(durations, slot) | pair (i, j), i<j, sum == slot, smallest j then smallest i; None | complement map | same-index, largest-i |
| 15 | med | endpoint_stats(calls) | calls [(endpoint, ms)] -> {ep: {count,min,max,total}} | multi-aggregate | min-init-zero, count-off |
| 16 | med | ready_tests(deps, done) | not done, all prereqs done; input order; prereq absent from deps is just a name | subset check | any-instead-of-all, includes-done |
| 17 | med | deep_merge(base, override) | dicts merge recursively, others (incl. lists) replaced; inputs not mutated/aliased | recursive merge | shallow, mutates-base |
| 18 | med | TtlCache set/get with explicit now | valid while now < set_time+ttl; overwrite resets | dict + timestamps | inclusive-expiry, no-reset |
| 19 | med | left_join(left, right, key) | each left row x each matching right row; no match -> left row alone; right wins on clash | hash join | inner-join, first-match-only |
| 20 | med | search_docs(docs, query) | ids of docs containing all query words (case-insens), sorted; empty query -> [] | inverted index | any-word, case-sensitive |
| 21 | hard | count_spans_sum(values, k) | contiguous non-empty subarrays summing to k, negatives ok, 200k | prefix-sum hash | missing-initial-zero, quadratic |
| 22 | hard | LfuCache(capacity) | evict least frequently used, ties least recently used; put on existing counts as use; capacity 0 stores nothing | freq buckets | lru-only, tie-most-recent, slow-scan |
| 23 | hard | run_order(deps) | topological order, ties alphabetical; prereq-only names are nodes; cycle -> ValueError | Kahn + heap | no-tiebreak, cycle-ignored |
| 24 | hard | longest_run(ids) | longest run of consecutive ints (dups ignored), tie smaller start, returns list; 200k | set, run starts | no-dedupe, quadratic |
| 25 | hard | merge_accounts(accounts) | account = email list; accounts sharing any email merged transitively; sorted unique, groups sorted | union-find | no-transitive, unsorted |
| 26 | hard | FirstUnique add/first | first value seen exactly once so far, else None; 100k | dict + deque lazy | picks-first-seen, slow-scan |
| 27 | hard | count_exact_distinct(values, k) | subarrays with exactly k distinct values, 100k | atMost(k) - atMost(k-1) | at-most, quadratic |
| 28 | hard | VersionedConfig set/get(key, t) | latest value with set time <= t per key; None before first | dict of lists + bisect | strict-less, global-latest |
| 29 | hard | TxStore nested transactions | begin/set/get/delete/commit/rollback; commit merges into parent; rollback undoes one level | layered dicts | commit-discards-parent, rollback-all |
| 30 | hard | count_quads(a, b, c, d) | index tuples with a[i]+b[j]+c[k]+d[l]==0, lists up to 300 | pair-sum dict | counts-distinct-sums, quartic |

Self-review: counting, set ops, merge, lookup, grouping, join, index, cache, then algorithms with different engines (prefix hash, buckets, graph, union-find, window, bisect, layers, meet-in-the-middle). Hard tasks are not stdlib one-liners: LFU, TxStore, VersionedConfig need own structure; run_order's alphabetical tie rule rules out graphlib.
