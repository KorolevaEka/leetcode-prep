import { PGlite } from "@electric-sql/pglite";
import * as sql from "../../web/runners/sql.js";

sql.init(PGlite);
export const execute = sql.execute;
