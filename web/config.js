export const SUPABASE_URL = "https://gmcueqiqqgtvaedwrilm.supabase.co";
export const SUPABASE_KEY = "sb_publishable_VRmuzMkRX8rmUU0K1OcRqw_9bD3qeHU";

export async function createSupabase() {
  const { createClient } = await import("https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/+esm");
  return createClient(SUPABASE_URL, SUPABASE_KEY, {
    auth: { flowType: "pkce", detectSessionInUrl: true, persistSession: true },
  });
}
