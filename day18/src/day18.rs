// SPDX-FileCopyrightText: 2023 Sebastian Andersson <sebastian@bittr.nu>
//
// SPDX-License-Identifier: GPL-3.0-or-later

use aoc_runner_derive::{aoc, aoc_generator};

use super::world::*;
use std::collections::HashMap;
// use std::collections::HashSet;
// use rayon::prelude::*;

type SolutionType = usize;

type EIdx = u8;

#[aoc_generator(day18)]
pub fn input_generator(input: &str) -> Map {
    Map::from_string(input)
}

fn is_walkable(c: u8) -> bool {
    c != b'#'
}

fn is_vertex(map: &Map, pos: Point, c: u8) -> bool {
    if is_walkable(c) {
        if c != b'.' {
            return true;
        }
        let mut count = 0;
        use Dir::*;
        for dir in [North, South, East, West] {
            let new_pos = pos.walk(dir);
            if let Some(c) = map.get_at(new_pos) {
                if is_walkable(c) {
                    count += 1;
                    if count > 2 {
                        return true;
                    }
                }
            }
        }
    }
    false
}

fn get_key_value(c: u8) -> u32 {
    if c.is_ascii_lowercase() {
        1 << u32::from(c - b'a')
    } else {
        0
    }
}

fn get_door_value(c: u8) -> u32 {
    if c.is_ascii_uppercase() {
        1 << u32::from(c - b'A')
    } else {
        0
    }
}

fn get_all_keys(map: &Map, verticies: &[Point]) -> u32 {
    let mut keys = 0;
    for vertex in verticies {
        let c = map.get_at_unchecked(*vertex);
        keys |= get_key_value(c);
    }
    keys
}

fn create_edges(
    map: &Map,
    verticies: &[Point],
    pos_to_vertex: &HashMap<Point, EIdx>,
) -> Vec<Vec<(EIdx, u16)>> {
    verticies
        .iter()
        .map(|&pos| {
            let mut frontier = Vec::new();
            let mut edges = Vec::new();
            use Dir::*;
            for dir in [North, South, East, West] {
                let new_pos = pos.walk(dir);
                if is_walkable(map.get_at_unchecked(new_pos)) {
                    frontier.push((0, pos, new_pos));
                }
            }
            while let Some((mut steps, old_pos, pos)) = frontier.pop() {
                steps += 1;
                if let Some(next_node) = pos_to_vertex.get(&pos) {
                    edges.push((*next_node, steps));
                } else {
                    for dir in [North, South, East, West] {
                        let new_pos = pos.walk(dir);
                        if new_pos != old_pos && is_walkable(map.get_at_unchecked(new_pos)) {
                            frontier.push((steps, pos, new_pos));
                        }
                    }
                }
            }
            edges
        })
        .collect()
}

#[aoc(day18, part1)]
pub fn solve_part1(map: &Map) -> SolutionType {
    let verticies: Vec<_> = map
        .iter()
        .filter_map(|(pos, c)| {
            if is_vertex(map, pos, c) {
                Some(pos)
            } else {
                Option::None
            }
        })
        .collect();

    assert!(verticies.len() < usize::from(EIdx::MAX));

    let pos_to_vertex: HashMap<_, _> = verticies
        .iter()
        .enumerate()
        .map(|(k, &v)| (v, EIdx::try_from(k).expect("fits")))
        .collect();

    let edges = create_edges(map, &verticies, &pos_to_vertex);

    let start = map.find(b'@')[0];
    let start = pos_to_vertex.get(&start).expect("Start is a vertex");

    let all_keys = get_all_keys(map, &verticies);

    let mut frontier = Vec::new();
    frontier.push((0i32, 0, *start));

    let mut visited = HashMap::new();

    let mut least_steps = i32::MAX;
    while let Some((steps, mut keys, node)) = frontier.pop() {
        let c = map.get_at_unchecked(verticies[usize::from(node)]);
        let key = get_key_value(c);
        keys |= key;

        if keys == all_keys {
            if steps < least_steps {
                least_steps = steps;
            }
            continue;
        }

        if let Some(old_steps) = visited.get(&(node, keys)) {
            if *old_steps <= steps {
                continue;
            }
        }
        visited.insert((node, keys), steps);

        let door = get_door_value(c);

        if door != (door & keys) {
            // Can't pass door yet
            continue;
        }

        for &(new_node, new_steps) in &edges[node as usize] {
            frontier.push((
                steps + i32::try_from(new_steps).expect("fits"),
                keys,
                new_node,
            ));
        }
    }

    SolutionType::try_from(least_steps).expect("A positive answer")
}

#[aoc(day18, part2)]
pub fn solve_part2(map: &Map) -> SolutionType {
    SolutionType::try_from(map.get_height()).expect("answer")
}
